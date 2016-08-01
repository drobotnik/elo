console.log('hello world')
var container = document.getElementById('visualization');

var groups = new vis.DataSet();
groups.add({
  id: 0,
  content: 'why?'
});

groups.add({
  id: 1,
  content: 'doodoo'
});

var items = [
  {x: '2014-06-13', y: 30, group: 0},
  {x: '2014-06-15', y: 15, group: 0},
  {x: '2014-06-10', y: 100, group: 0},
  {x: '2014-06-12', y: 200, group: 1},
  {x: '2014-06-14', y: 10, group: 1},
  {x: '2014-06-16', y: 30, group: 1}
];

var dataset = new vis.DataSet(items);

var options = {
  legend: true,
  start: '2014-06-09',
  end: '2014-06-18'
};
var graph2d = new vis.Graph2d(container, dataset, groups, options);
