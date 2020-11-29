function BuildStart(variableID) {
  d3.json("data/samples.json").then(function (data) {
    console.log(data);
    console.log(data)
    var names = data.names;
    console.log(names)
    // var samples = data.samples;
    var select = d3.select("#selDataset");
    names.forEach(function (name) {
      select.append("option").text(name).property("value", name);
    })
    BuildBarChart(data, variableID);
    BuildBubbleChart(data, variableID);
    BuildDemographicInfo(data, variableID);
    BuildGaugeChart(data, variableID)
  })
};
BuildStart(940);


function optionChanged() {
  var dropdownmenu = d3.select("#selDataset");
  var variableID = dropdownmenu.property("value");
  console.log(variableID);
  Buildingfunction(variableID)
};


function BuildBarChart(data, variableID) {
  var samples = data.samples;
  var dataId = samples.filter(sample => sample.id == variableID);
  var Ids10 = dataId[0].otu_ids.slice(0, 10);
  var IdsAsString = Ids10.map(Id => "Operational Taxonomic Units" + Id);
  var sample_value10 = dataId[0].sample_values.slice(0, 10).reverse();
  var sample_labels10 = dataId[0].otu_labels.slice(0, 10);
  var trace1 = {
    x: sample_value10,
    y: IdsAsString,
    type: 'bar',
    orientation: "h",
    text: sample_labels10,
    marker: {
      color: 'blue'
    }
  };

  var data = [trace1];

  var layout = {
    title: 'Top 10 Operational Taxonomic Units',
    font: {
      family: 'Raleway, sans-serif'
    },
    showlegend: false,
    yaxis: {
      zeroline: false,
      gridwidth: 3
    },
    bargap: 0.2
  };

  Plotly.newPlot("bar", data, layout);
};


function BuildBubbleChart(data, variableID) {
  var samples = data.samples;
  var dataId = samples.filter(sample => sample.id == variableID);
  var otu_id = dataId[0].otu_ids;
  var sample_value = dataId[0].sample_values;
  var sample_labels10 = dataId[0].otu_labels;
  var trace1 = {
    x: otu_id,
    y: sample_value,
    mode: 'markers',
    marker: {
      color: ['rgb(93, 164, 214)', 'rgb(255, 144, 14)', 'rgb(44, 160, 101)', 'rgb(255, 65, 54)'],
      opacity: [1, 0.8, 0.6, 0.4],
      size: [40, 60, 80, 100]
    }
  };

  var data = [trace1];

  var layout = {
    title: 'Top 10 Operational Taxonomic Units',
    showlegend: false,
    height: 600,
    width: 1140
  };
  Plotly.newPlot('bubblechart', data, layout);

};

function BuildDemographicInfo(data, variableID) {
  var metademo = data.metadata.filter(demo => demo.id == variableID)[0];
  var demograph = d3.select("#sample-metadata");
  demograph.html("");
  Object.entries(metademo).forEach(([key, value]) => {
    var info = demograph.append("p");
    info.text(`${key}: ${value}`);
  });

};



function Buildingfunction(variableID) {
  d3.json("data/samples.json").then(function (data) {
    BuildBarChart(data, variableID);
    BuildBubbleChart(data, variableID);
    BuildDemographicInfo(data, variableID);
    BuildGaugeChart(data, variableID);
  }

  )
};



function BuildGaugeChart(data, variableID) {
  var metademo = data.metadata.filter(demo => demo.id == variableID)[0];
  var frequency = metademo.wfreq;



  var data = [
    {
      type: 'pie',
      showlegend: true,
      hole: 0.4,
      rotation: 90,
      // values: dataId[0].sample_values,
      // text: dataId[0].otu_labels,
      values: [81 / 9, 81 / 9, 81 / 9, 81 / 9, 81 / 9, 81 / 9, 81 / 9, 81 / 9, 81 / 9, 81],
      text: ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9'],
      direction: 'clockwise',
      textinfo: 'text',
      textposition: 'inside',
      marker: {
        colors: ['', '', '', '', '', '', '', '', '', 'white'],
        labels: ['0-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7', '7-8', '8-9'],
        hoverinfo: 'label'

      }
    }
  ];



  var degrees = 50, radius = 0.9
  var radians = degrees * Math.PI / 180
  console.log(radians)
  var x = -1 * radius * Math.cos(radians) * frequency
  var y = radius * Math.sin(radians)
  console.log(x);
  console.log(y);
  console.log(frequency);
  var gaugeLayout = {
    shapes: [{
      type: 'line',
      x0: 0.5,
      y0: 0.5,
      x1: 0.6,
      y1: 0.6,
      line: {
        color: 'black',
        width: 5
      }
    }],
    title: 'Belly Button Washing Frequency',
    xaxis: { visible: false, range: [0, 1] },
    yaxis: { visible: false, range: [0, 1] }
  }

  Plotly.plot('gauge', data, gaugeLayout)

};