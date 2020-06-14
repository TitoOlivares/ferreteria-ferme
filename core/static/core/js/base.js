$(document).ready(function () {
    $('#data').DataTable({
        language: {
            'sSearch': 'Buscar',
            'info': 'Mostrando registros del _START_ al _END_ de un total de _TOTAL_ registros',
            'lengthMenu': 'Mostrar _MENU_ registros',
            'oPaginate': {
                'sNext': 'Siguiente',
                'sPrevious': 'Anterior'
            }
        },
        responsive: "true",
        dom: 'Bfrtilp',
        buttons: [
            {
                extend: 'excel',
                text: '<i class="fas fa-file-excel"></i>',
                titleAttr: 'Exportar a Excel',
                className: 'btn btn-success'
            },
            {
                extend: 'pdf',
                text: '<i class="fas fa-file-pdf"></i>',
                titleAttr: 'Exportar a PDF',
                className: 'btn btn-danger'
            },
            {
                extend: 'print',
                text: '<i class="fas fa-print"></i>',
                titleAttr: 'Imprimir',
                className: 'btn btn-success'
            },
        ]
    });
});