# Responsive Table
Sometimes you need to display data in a table. Tables should look good in portrait, too!
Though frequently shunned, HTML tables have a legitimate purpose in modern web development: displaying collections of data.
While many have adopted HTML + CSS + JS libraries, we should be able to use just HTML & CSS to display data in a responsive way.
We can.

### A Standard Table
The challenge with a responsive table is that table column headers must always be near the relevant
column data. With CSS, we can have all `tr` & `td` elements stack via CSS `display: block;`. The columns would
be at the top of the stack & all values below them. This is not ideal.

```html
<style>
  table tr,
  table td {
    display: block;
  }
</style>
<table>
    <thead>
        <tr>
            <th>Column Foo</th>
            <th>Column Bar</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Baz</td>
            <td>Qux</td>
        </tr>
    </tbody>
</table>
```
<a href="https://yesnoio.github.io/responsive-table/fail.html">See the Result</a>

### A Responsive Table
In order to have a responsive table, column labels need to be near column cell data. We need to add these
labels to each cell -- and hide them all by default.

```html
<style>
  table.responsive td .label {
    display: none;
  }
</style>
<table class="responsive">
    <thead>
        <tr>
            <th>Column Foo</th>
            <th>Column Bar</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><span class="label">Column Foo</span><span class="data">Baz</span></td>
            <td><span class="label">Column Bar</span><span class="data">Qux</span></td>
        </tr>
    </tbody>
</table>
```
<a href="https://yesnoio.github.io/responsive-table/cell-labels-added.html">See the Result</a>

With that done, we are able to use just CSS to show/hide & arrange the display as needed:
```css
/* Some Basics */
table.responsive {
  width: 100%;
}
table.responsive th {
  background-color: #ddd;
}

/* Hide cell labels by default */
table.responsive td .label {
  display: none;
}

/* Apply the contained CSS only to narrow viewports via a Media Query */
@media screen and (max-width:640px) {
  /* Hide the table header */
  table.responsive thead {
      display: none;
  }
  
  /* Vertically stack the table elements */
  table.responsive tbody th,
  table.responsive tbody td {
      display: block;
  }
  
  /* Make all cell column span tags visible & change them from inline-block to block */
  table.responsive td span {
    display: block;
  }
  
  /* Make all cell labels look like column headers  */
  table.responsive td .label {
      background-color: #ddd;
      font-weight: bold;
      text-align: center;
  }
}
```
<a href="https://yesnoio.github.io/responsive-table/success.html">See the Result</a>

The tables will look great in both portrait & landscape viewports. Huzzah.

*fin*
