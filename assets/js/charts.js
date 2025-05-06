const chart_1 = document.getElementById("chart_1").getContext("2d");
const chart_2 = document.getElementById("chart_2").getContext("2d");
const chart_3 = document.getElementById("chart_3").getContext("2d");


new Chart(chart_1, {
    type: "line",
    

    data: {
        labels: ["Noviembre", "Diciembre", "Enero", "Febrero", "Marzo", "Abril"],
        datasets: [
            {
                label: "Crecimiento del 150% en nuevos usuarios en los últimos 6 meses.",
                backgroundColor: "#00628D",
                borderColor: "#00628D",
                data: [500, 2000, 5000, 10000, 15000, 20000],
                fill: false,
            },
        ],
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
            labels: {
                fontColor: "white" // color de las letras de la leyenda
            }
        },
        scales: {
            xAxes: [{
                ticks: {
                    fontColor: "white" // color de etiquetas eje X
                }
            }],
            yAxes: [{
                ticks: {
                    fontColor: "white" // color de etiquetas eje Y
                }
            }]
        }
    }


})



new Chart(chart_2, {
    type: "doughnut",
    data: {
        labels: ["Laboratorio", "Publicaciones", "Interaccion"],
        datasets:[
            {
                label: "Variedad de actividades realizadas por los estudiantes",
                data: [300, 1000, 500],
                backgroundColor: [
                    "#FF6384",
                    "#00628D",
                    "#FFCE56",
                ],
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: true,
            },
        },
    },
});


new Chart(chart_3, {
    type: "line",
    data: {
        labels: ["Enero", "Febrero", "Marzo", "Abril"],
        datasets:[
            {
                label: "Más de 10,000 estudiantes conectados en el ultimo mes",
                backgroundColor: "#00628D",
                borderColor: "#00628D",
                data: [500, 2000, 5000, 10000],
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: true,
            },
        },
    },


});