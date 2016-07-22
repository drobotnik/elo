console.log('hello world')
var container = document.getElementById('visualization');

var groups = new vis.DataSet();
groups.add({
        id: 0,
        group: "why",
        options: {
            drawPoints: {
                style: 'square' // square, circle
            },
            shaded: {
                orientation: 'bottom' // top, bottom
            }
        }});
groups.add({
  id: 1,
  group: 'doodoo'
})

var items = [
  {x: '2014-06-11', y: 100, group: 0},
  {x: '2014-06-12', y: 200, group: 1},
  {x: '2014-06-13', y: 30, group: 0},
  {x: '2014-06-14', y: 10, group: 1},
  {x: '2014-06-15', y: 15, group: 0},
  {x: '2014-06-16', y: 30, group: 1}
];

var dataset = new vis.DataSet(items);

var options = {
  legend: true,
  start: '2014-06-10',
  end: '2014-06-18'
};
var graph2d = new vis.Graph2d(container, dataset, options);
