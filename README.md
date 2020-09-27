<h1>Bulk Certificate Generator</h1>

<p>
   ![Sample Certificate](sample.png)
   ![Image of Yaktocat](https://octodex.github.com/images/yaktocat.png)

**Run Command ```python certificate_generator.py```**

**Required Libraries**
- Pandas ```pip install pandas```
- PIL   ```pip install image```

**Instructions**
* Data of bulk contacts in csv format (renamed as data.csv)
    * only one column must have all names
    * First row of column must be named as *name* (refer data.csv)
* A Certificate template (template.jpg)
* Must adjust the location of Text using *location* in code (hit and trial while producing)
    * Use MS PAINT to determine coordinate of beginning of text in certificate (bottom left pane of ms paint)
* You can output certificate in any format (PDF default)
