// Class definition

var KTFormWidgetsValidation = function () {
    // Private functions
    var validator;


    var _initWidgets = function () {
        // Initialize Plugins

        $('#kt_datepicker_3, #kt_datepicker_3_validate').datepicker({
            rtl: false,
            format: 'yyyy-mm-dd',
            todayBtn: "linked",
            clearBtn: true,
            todayHighlight: true,
            templates: {
                leftArrow: '<i class="la la-angle-left"></i>',
                rightArrow: '<i class="la la-angle-right"></i>'
            }
        }).on('changeDate', function (e) {
            // Revalidate field
            validator.revalidateField('date');
        }).on('changeDate', function (e) {
            // Revalidate field
            validator.revalidateField('spk');
        }).on('changeDate', function (e) {
            // Revalidate field
            validator.revalidateField('deadline');
        });

        // Select2 user
        $('#kt_select2_3').select2({
            placeholder: "Select a user",
        });

        $('#kt_select2_3').on('change', function () {
            // Revalidate field
            validator.revalidateField('users');
        });

        $('#iname').on('change', function () {
            // Revalidate field
            validator.revalidateField('name');
        });
        $('#ikode').on('change', function () {
            // Revalidate field
            validator.revalidateField('kode');
        });

        // Select2 paper

        $('#kt_select2_4').select2({
            placeholder: "Select a paper",
        });

        $('#kt_select2_4').on('change', function () {
            // Revalidate field
            validator.revalidateField('paper');
        });

        // Select2 paper

        $('#kt_select2_5').select2({
            placeholder: "Select a gram",
        });

        $('#kt_select2_5').on('change', function () {
            // Revalidate field
            validator.revalidateField('gramatur');
        });

        // Select2 laminasi

        $('#kt_select2_6').select2({
            placeholder: "Select a laminasi",
        });

        $('#kt_select2_6').on('change', function () {
            // Revalidate field
            validator.revalidateField('laminasi');
        });

        // Select2 finishing

        $('#kt_select2_7').select2({
            placeholder: "Select a finishing",
        });

        $('#kt_select2_7').on('change', function () {
            // Revalidate field
            validator.revalidateField('finishing');
        });

        // Select2 sisi

        $('#kt_select2_8').select2({
            placeholder: "Select a Sisi",
        });

        $('#kt_select2_8').on('change', function () {
            // Revalidate field
            validator.revalidateField('sisi');
        });

        // Select2 bahan

        $('#kt_select2_90').select2({
            placeholder: "Pilih ukuran bahan",
        });

        $('#kt_select2_90').on('change', function () {
            // Revalidate field
            validator.revalidateField('ukuran_bahan');
        });

        // untuk kalkulator
        // Select2 kertas

        $('#kt_select2_70').select2({
            placeholder: "pilih kertas",
        });

        $('#kt_select2_70').on('change', function () {
            fetchHarga();
        });

        $('#kt_select2_72').select2({
            placeholder: "pilih ukuran",
        });

        $('#kt_select2_72').on('change', function () {
            // Revalidate field
            // validator.revalidateField('ukuran_kertas');
            fetchHarga();
        });
        $('#kertas_input').on('input', function () {
            fetchHarga();
        });


        // untuk jasa potong
        $('#kt_select2_82').select2({
            placeholder: "Ongkos Cetak",
        });

        $('#kt_select2_82').on('change', function () {
            // Revalidate field
            // validator.revalidateField('ukuran_kertas');
            fetchHarga();
        });

        // untuk set warna
        $('#kt_select2_setwarna').select2({
            placeholder: "Set Warna",
        });

        $('#kt_select2_setwarna').on('change', function () {
            fetchHarga();
        });
        $('#set_input').on('input', function () {
            fetchHarga();
        });

        // untuk harga dreg
        $('#jumlah_dreg').on('input', function () {
            fetchHarga();
        });

        $('#ukuran_dreg').select2({
            placeholder: "Pilih dreggggg",
        });

        $('#ukuran_dreg').on('change', function () {
            fetchHarga();
        });



        // untuk jasa laminasi
        $('#kt_select2_83').select2({
            placeholder: "Pilih Laminasi",
        });

        $('#kt_select2_83').on('change', function () {
            fetchHarga();
        });

        $('#laminasi_input').on('input', function () {
            fetchHarga();
        });


        // untuk jasa finishing
        $('#kt_select2_54').select2({
            placeholder: "Pilih Finishinggg",
            multiple: true,
        });

        $('#kt_select2_54').on('change', function () {
            fetchHarga();
        });
        $('#finishing_input').on('input', function () {
            fetchHarga();
        });

        // untuk lain lain
        $('#lain_input').on('input', function () {
            fetchHarga();
        });
        
        // untuk hitung margin
        $('#margin_input').on('input', function () {
            fetchHarga();
        });

        // button for generating details table
        $('#generate_table').on('click', function() {
            const detailsTable = $('#details-table');
            const tableBody = detailsTable.find('tbody');

            // Clear any existing rows
            tableBody.empty();

            // Add rows for each item
            addTableRow(tableBody, 'Paper', `${$('#kt_select2_70').val()} (${$('#kt_select2_72').val()})`, $('#kertas_input').val(), $('#harga_display').text());
            addTableRow(tableBody, 'Production Cost', `${$('#kt_select2_82').val()} (${$('#kt_select2_setwarna').val()} sets)`, $('#set_input').val(), $('#ongkos_display').text());
            addTableRow(tableBody, 'Dreg', `${$('#jumlah_dreg').val()} pieces (${$('#ukuran_dreg').val()} rupiah)`, $('#jumlah_dreg').val(), $('#dreg_display').text());
            addTableRow(tableBody, 'Lamination', $('#kt_select2_83').val(), $('#laminasi_input').val(), $('#laminasi_display').text());
            addTableRow(tableBody, 'Finishing', $('#kt_select2_54').val(), $('#finishing_input').val(), $('#finishing_display').text());
            addTableRow(tableBody, 'Cutting Blade', '', '', $('#pisau_display').text());

            // Add margin row
            const margin = parseFloat($('#margin_input').val()) || 0;
            const marginAmount = parseFloat($('#total_cost_display').text().replace(/[^0-9.-]+/g, "")) * (margin / 100);
            addTableRow(tableBody, 'Margin', `${margin}%`, '', `Rp ${marginAmount.toLocaleString('id-ID')}`);

            // Add total price row
            addTableRow(tableBody, 'Total Price', '', '', $('#total_cost_display').text());

            // Toggle the table visibility
            detailsTable.toggle();
        });

        function addTableRow(tableBody, item, description, quantity, cost) {
            const row = $('<tr>');
            row.append($('<td>').text(item));
            row.append($('<td>').text(description));
            row.append($('<td>').text(quantity));
            row.append($('<td>').text(cost));
            tableBody.append(row);
        }

        function fetchHarga() {
            var selectedTipe = $('#kt_select2_70').val();
            var selectedUkuran = $('#kt_select2_72').val();
            var kertasQuantity = parseFloat($('#kertas_input').val()) || 0;
            var selectedOngkos = $('#kt_select2_82').val();
            var selectedJumlahDreg = parseFloat($('#jumlah_dreg').val());
            var selectedUkuranDreg = $('#ukuran_dreg').val();
            var selectedSetWarna = $('#kt_select2_setwarna').val();
            var jumlahSet = parseFloat($('#set_input').val()) || 0;
            var selectedLaminateType = $('#kt_select2_83').val();
            var laminateQuantity = parseFloat($('#laminasi_input').val()) || 0;
            var selectedFinishing = $('#kt_select2_54').val();
            var finishingQuantity = parseFloat($('#finishing_input').val()) || 0;
            var lainLainPrice = parseFloat($('#lain_input').val()) || 0;
            var margin = parseFloat($('#margin_input').val()) || 0;  // Get margin value from input field (assuming it exists)


          
            $.ajax({
              url: '/calculate/',
              method: 'GET',
              data: {
                'tipe_kertas': selectedTipe,
                'ukuran_kertas': selectedUkuran,
                'kertas_quantity': kertasQuantity,
                'production_cost': selectedOngkos,
                'set_warna': selectedSetWarna,
                'jumlah_set': jumlahSet,
                'jumlah_dreg': selectedJumlahDreg,
                'ukuran_dreg': selectedUkuranDreg,
                'laminate_type': selectedLaminateType,
                'laminate_quantity': laminateQuantity,
                'tipe_finishing': selectedFinishing.join(','),
                'finishing_quantity': finishingQuantity,
              },
              success: function (response) {
                if (response.harga !== null) {
                    var totalHargaKertas = parseFloat(response.harga) * kertasQuantity;
                    $('#harga_display').text('Rp ' + totalHargaKertas.toLocaleString('id-ID'));
                } else {
                  $('#harga_display').text('Harga Tidak Tersedia');
                }
          
                if (response.production_cost !== null) {
                    var totalOngkosCetak = parseFloat(response.production_cost) * jumlahSet
                  $('#ongkos_display').text('Rp ' + totalOngkosCetak.toLocaleString('id-ID'));
                } else {
                  $('#ongkos_display').text('Harga Tidak Tersedia');
                }

                if (selectedUkuranDreg !== "" && !isNaN(selectedJumlahDreg)) {
                    var dregArea = selectedJumlahDreg;
                    var dregCost = dregArea * parseFloat(selectedUkuranDreg);
                    $('#dreg_display').text('Rp ' + dregCost.toLocaleString('id-ID'));
                  } else {
                    $('#dreg_display').text('Harga Tidak Tersedia');
                  }

                if (response.laminateCost !== null) {
                    var laminateCost = parseFloat(selectedUkuran) * parseFloat(selectedLaminateType) * laminateQuantity;
                    $('#laminasi_display').text('Rp ' + laminateCost.toLocaleString('id-ID'));
                } else {
                    $('#laminasi_display').text('Harga Tidak Tersedia');  // Display placeholder if data incomplete
                }

                if (response.pisauPrice !== null){
                    var pisauPrice = parseFloat(selectedOngkos);
                    $('#pisau_display').text('Rp ' + pisauPrice.toLocaleString('id-ID'));
                } else {
                    $('#pisau_display').text('Harga Tidak Tersedia');  // Display placeholder if data incomplete
                }

                if (response.harga_finishing !== null) {
                    var finishingCost = 0;
                    if (typeof response.harga_finishing === 'object' && response.harga_finishing !== null) {
                    for (var i = 0; i < response.harga_finishing.length; i++) {
                        finishingCost += parseFloat(response.harga_finishing[i]) * finishingQuantity;
                    }
                    } else {
                    finishingCost = parseFloat(response.harga_finishing) * finishingQuantity;
                    }
                    $('#finishing_display').text('Rp ' + finishingCost.toLocaleString('id-ID'));
                } else {
                    $('#finishing_display').text('Price data not available');
                }

                // Calculate the total cost
                var totalCost = 0;
                if (response.harga !== null) {
                    totalCost += parseFloat(response.harga);
                }
                if (response.production_cost !== null) {
                    totalCost += parseFloat(response.production_cost);
                }
                if (response.harga_dreg !== null) {
                    totalCost += parseFloat(response.harga_dreg);
                }
                if (response.harga_laminasi !== null) {
                    totalCost += parseFloat(response.harga_laminasi);
                }
                
                if (response.harga_finishing !== null) {
                    if (typeof response.harga_finishing === 'object' && response.harga_finishing !== null) {
                      for (var i = 0; i < response.harga_finishing.length; i++) {
                        totalCost += parseFloat(response.harga_finishing[i]);
                      }
                    } else {
                      totalCost += parseFloat(response.harga_finishing);
                    }
                }


                // Update the total cost display
                var totalCost = totalHargaKertas + totalOngkosCetak + dregCost + laminateCost + finishingCost + pisauPrice;
                $('#pisau_display').text('Rp ' + pisauPrice.toLocaleString('id-ID'));
                // Calculate margin amount
                var marginAmount = totalCost * (margin / 100);

                // Add margin to total cost
                totalCost = totalCost + marginAmount;
                $('#total_cost_display').text('Rp ' + totalCost.toLocaleString('id-ID')); 

                // Update existing total cost display (without margin)
                // $('#total_cost_display').text('Rp ' + (totalCost - marginAmount).toLocaleString('id-ID'));

                // Add a new element to display the final cost with margin
                // $('#total_cost_display').parent().append('<span class="text-danger">Total Cost with Margin: Rp ' + totalCost.toLocaleString('id-ID') + '</span>');


                
              },
              error: function () {
                $('#harga_display').text('Kombinasi harga tidak tersedia');
                $('#ongkos_display').text('Kombinasi harga tidak tersedia');
                $('#dreg_display').text('Kombinasi harga tidak tersedia');
                $('#laminasi_display').text('Kombinasi harga tidak tersedia');
                $('#finishing_display').text('Kombinasi harga tidak tersedia');
                $('#total_cost_display').text('Kombinasi harga tidak tersedia');
              }
            });
          }


        // Select2 bahan cetak max

        // $('#kt_select2_10').select2({
        //     placeholder: "Pilih ukuran bahan cetak max",
        // });

        // $('#kt_select2_10').on('change', function () {
        //     // Revalidate field
        //     validator.revalidateField('ukuran_bahan_cetak_max');
        // });

        $('#ijumplat').on('change', function () {
            // Revalidate field
            validator.revalidateField('jumlah_plat');
        });

        $('#iukbahancetak').on('change', function () {
            // Revalidate field
            validator.revalidateField('uk_bahan_cetak');
        });
        $('#ijumcetak').on('change', function () {
            // Revalidate field
            validator.revalidateField('jumlah_cetak');
        });
        $('#ijumwaste').on('change', function () {
            // Revalidate field
            validator.revalidateField('jumlah_waste');
        });
        $('#ijumkertas').on('change', function () {
            // Revalidate field
            validator.revalidateField('jumlah_kertas');
        });

    }

    var _initValidation = function () {
        // Validation Rules
        validator = FormValidation.formValidation(
            document.getElementById('add_board_from'),
            {
                fields: {
                    name: {
                        validators: {
                            notEmpty: {
                                message: 'Nama harus diisi'
                            },
                            stringLength: {
                                min: 1,
                                max: 50,
                                message: 'Silakan masuk ke menu dalam rentang panjang teks 1 dan 50'
                            }
                        }
                    },
                    kode: {
                        validators: {
                            notEmpty: {
                                message: 'Kode harus diisi'
                            },
                            stringLength: {
                                min: 1,
                                max: 50,
                                message: 'Silakan masuk ke menu dalam rentang panjang teks 1 dan 50'
                            }
                        }
                    },
                    paper: {
                        validators: {
                            notEmpty: {
                                message: 'Pilih Jenis Kertas'
                            }
                        }
                    },
                    gramatur: {
                        validators: {
                            notEmpty: {
                                message: 'Pilih gramatur'
                            }
                        }
                    },
                    laminasi: {
                        validators: {
                            notEmpty: {
                                message: 'Pilih Jenis Laminasi'
                            }
                        }
                    },
                    finishing: {
                        validators: {
                            notEmpty: {
                                message: 'Pilih Jenis finishing'
                            }
                        }
                    },
                    sisi: {
                        validators: {
                            notEmpty: {
                                message: 'Pilih Jenis Sisi'
                            }
                        }
                    },
                    jumlah_plat: {
                        validators: {
                            notEmpty: {
                                message: 'Jumlah plat harus diisi'
                            },
                            stringLength: {
                                min: 1,
                                max: 20,
                                message: 'Silakan masuk ke menu dalam rentang panjang teks 1 dan 50'
                            }
                        }
                    },
                    uk_bahan_cetak: {
                        validators: {
                            notEmpty: {
                                message: 'Ukuran bahan cetak harus diisi'
                            },
                            stringLength: {
                                min: 1,
                                max: 20,
                                message: 'Silakan masuk ke menu dalam rentang panjang teks 1 dan 50'
                            }
                        }
                    },
                    jumlah_cetak: {
                        validators: {
                            notEmpty: {
                                message: 'Jumlah cetak harus diisi'
                            },
                            stringLength: {
                                min: 1,
                                max: 20,
                                message: 'Silakan masuk ke menu dalam rentang panjang teks 1 dan 50'
                            }
                        }
                    },
                    jumlah_waste: {
                        validators: {
                            notEmpty: {
                                message: 'Jumlah waste harus diisi'
                            },
                            stringLength: {
                                min: 1,
                                max: 20,
                                message: 'Silakan masuk ke menu dalam rentang panjang teks 1 dan 50'
                            }
                        }
                    },
                    jumlah_kertas: {
                        validators: {
                            notEmpty: {
                                message: 'Jumlah kertas harus diisi'
                            },
                            stringLength: {
                                min: 1,
                                max: 20,
                                message: 'Silakan masuk ke menu dalam rentang panjang teks 1 dan 50'
                            }
                        }
                    },
                    ukuran_bahan: {
                        validators: {
                            notEmpty: {
                                message: 'Pilih ukuran bahan'
                            },
                            stringLength: {
                                min: 1,
                                max: 20,
                                message: 'Silakan masuk ke menu dalam rentang panjang teks 1 dan 50'
                            }
                        }
                    },
                    date: {
                        validators: {
                            notEmpty: {
                                message: 'tanggal harus diisi'
                            }
                        }
                    },
                    users: {
                        validators: {
                            notEmpty: {
                                message: 'Pengguna harus diisi'
                            }
                        }
                    },
                },

                plugins: {
                    trigger: new FormValidation.plugins.Trigger(),

                    // Validate fields when clicking the Submit button
                    submitButton: new FormValidation.plugins.SubmitButton(),

                    // Submit the form when all fields are valid
                    // defaultSubmit: new FormValidation.plugins.DefaultSubmit(),

                    bootstrap: new FormValidation.plugins.Bootstrap()

                }
            }
        );

        $('#psubmit').on('click', function (e, options) {
            options = options || {};

            if (!options.flag) {
                e.preventDefault();

                validator.validate().then(function (status) {
                    if (status == 'Valid') {
                        swal.fire({
                            text: "All is cool! Now we submitted data to the Server",
                            icon: "success",
                            buttonsStyling: false,
                            confirmButtonText: "Ok, got it!",
                            customClass: {
                                confirmButton: "btn font-weight-bold btn-light-primary"
                            }
                        }).then(function () {
                            $('#psubmit').trigger('click', {flag: true});
                        });
                    } else {
                        swal.fire({
                            text: "Sorry, looks like there are some errors detected, please try again.",
                            icon: "error",
                            buttonsStyling: false,
                            confirmButtonText: "Ok, got it!",
                            customClass: {
                                confirmButton: "btn font-weight-bold btn-light-primary"
                            }
                        }).then(function () {
                            KTUtil.scrollTop();
                        });
                    }
                });
            } else {
                $("#add_board_from").submit();
            }
        });
    }

    return {
        // public functions
        init: function () {
            _initWidgets();
            _initValidation();
        }
    };
}();

jQuery(document).ready(function () {
    KTFormWidgetsValidation.init();
});
