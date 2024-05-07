from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from datetime import datetime
from task_manager.models import Project, KalkulatorCetak
from .models import ProjectInfo, UserInfo, UserInProject, PriceData, ProductionPrice, DregCost, LaminateCost, FinishingCost, PAPER_SIZE_CHOICES

class Calculate(View):
    def get(self, request):
        print('Request received:', request.GET)
        if not request.user.is_authenticated:
            return redirect('signIn')

        user = request.user
        projects = Project.objects.all()
        p_info_list = []
        u_info = UserInfo(user)
        user_in_projects = []

        for p in projects:
            if p.owner == user or user.id in p.get_members():
                p_info = ProjectInfo(p)
                u_info.analyze_project(p)
                p_info_list.append(p_info)
                user_in_projects.append(UserInProject(user, p))

        # untuk kertas
        tipe_kertas_choices = PriceData.objects.values_list('tipe_kertas', flat=True).distinct()
        ukuran_kertas_choices = PriceData.objects.values_list('ukuran_kertas', flat=True).distinct()

        # untuk harga cetak
        production_cost_choices = ProductionPrice.objects.values_list('production_cost', flat=True).distinct()
        set_warna_choices = ProductionPrice.objects.values_list('set_warna', flat=True).distinct()

        # untuk harga finishing 
        finishing_cost_choices = FinishingCost.objects.values_list('tipe_finishing', flat=True).distinct()

        # selected kertas
        selected_tipe_kertas = request.GET.get('tipe_kertas')
        selected_ukuran_kertas = request.GET.get('ukuran_kertas')

        # selected produsction cost
        selected_production_cost = request.GET.get('production_cost')
        selected_set_warna = request.GET.get('set_warna')

        # selected dreg cost 
        selected_jumlah_dreg = request.GET.get('jumlah_dreg')
        selected_ukuran_dreg = request.GET.get('ukuran_dreg')

        # selected laminasi cost
        selected_laminate_type = request.GET.get('laminate_type')

        # selected finishing cost 
        selected_finishing_cost = request.GET.get('tipe_finishing')

        harga = None
        production_cost_value = None
        dreg_cost_value = None
        laminate_cost_value = None
        finishing_cost_value = None

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            if selected_tipe_kertas  and selected_ukuran_kertas:
                try:
                    price_data = PriceData.objects.get(tipe_kertas=selected_tipe_kertas,
                                                       ukuran_kertas=selected_ukuran_kertas)
                    harga = price_data.harga
                except PriceData.DoesNotExist:
                    harga = None

            if selected_production_cost and selected_set_warna:
                try:
                    production_cost_data = ProductionPrice.objects.get(production_cost=selected_production_cost,
                                                                       set_warna=selected_set_warna)
                    production_cost_value = production_cost_data.harga_produksi
                except ProductionPrice.DoesNotExist:
                    production_cost_value = None

            if selected_jumlah_dreg and selected_ukuran_dreg:
                try:
                    dreg_cost_data = DregCost.objects.get(jumlah_dreg=selected_jumlah_dreg,
                                                          ukuran_dreg=selected_ukuran_dreg)
                    dreg_cost_value = dreg_cost_data.harga_dreg * float(selected_jumlah_dreg)
                except DregCost.DoesNotExist:
                    dreg_cost_value = None
            
            if selected_laminate_type:
                try:
                    laminate_cost_data = LaminateCost.objects.get(laminate_type=selected_laminate_type)
                    laminate_cost_value = laminate_cost_data.harga_laminasi
                except LaminateCost.DoesNotExist:
                    laminate_cost_value = None
            
            if selected_finishing_cost:
                try:
                    finishing_cost_data = FinishingCost.objects.filter(tipe_finishing__in=selected_finishing_cost.split(','))
                    finishing_cost_value = sum(fc.harga_finishing for fc in finishing_cost_data)
                except FinishingCost.DoesNotExist:
                    finishing_cost_value = None


            return JsonResponse({
                'harga': harga,
                'production_cost': production_cost_value,
                'harga_dreg': dreg_cost_value,
                'harga_laminasi': laminate_cost_value,
                'harga_finishing': finishing_cost_value
            })

        context = {
            "user": user,
            "first": user.username[0],
            "p_info": p_info_list,
            "u_info": u_info,
            "u_in_p": user_in_projects,
            'time': datetime.today(),
            "tipe_kertas_choices": tipe_kertas_choices,
            "ukuran_kertas_choices": PAPER_SIZE_CHOICES,
            "production_cost_choices": production_cost_choices,
            "set_warna_choices": set_warna_choices,
            "finishing_cost_choices": finishing_cost_choices,
            "selected_tipe_kertas": selected_tipe_kertas,
            "selected_ukuran_kertas": selected_ukuran_kertas,
            "selected_production_cost": selected_production_cost,
            "selected_set_warna": selected_set_warna,
            'selected_jumlah_dreg': selected_jumlah_dreg,
            'selected_ukuran_dreg': selected_ukuran_dreg,
            'selected_laminate_type': selected_laminate_type,
            "selected_finishing_cost": selected_finishing_cost,
            "harga": harga,
            "production_cost": production_cost_value,
            "harga_dreg": dreg_cost_value,
            "harga_laminasi": laminate_cost_value,
            "harga_finishing": finishing_cost_value,
        }

        print(f"harga laminasi {laminate_cost_value}")
        print(f"harga finishing {finishing_cost_value}")

        return render(request, 'calculate.html', context)