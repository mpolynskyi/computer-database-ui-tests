### Create computer with valid data, filter table by computer name, check saved values:
#### SetUp: reset fixtures (database values)
#### Steps:
1. Go to /computers <br>
   Expected result. I can see:
   * Table with computers, with pagination control
   * "Filter by computer name..." **filter input**
   * 2 buttons: **Filter by name button** near filter input, **Add a new computer button**
   * Text "574 computers found" on top of **filter input**
2. Click on **Add a new computer button** <br>
   Expected result: redirection on /computers/new to page with 'Add computer' form
3. Fill **Computer name field** with `test computer` value
4. Fill **Introduced field** with `2021-08-29` value
5. Fill **Discontinued field** with `2023-08-29` value
6. In **Company selector** choose `RCA` company
7. Click on **Create this computer button**<br>
Expected result:
   * Redirection to /computers page
   * Alert message "Done ! Computer test computer has been created"
   * Text "575 computers found" on top of alert message
8. Fill **filter input** with `test computer` value and click on **Filter by name button** <br>
Expected result.<br>
   In updated computer table I can see row with my created computer:
   * `test computer` in **Computer name column**
   * `2021-08-29` in **Introduced column**
   * `2023-08-29` in **Discontinued column**
   * `RCA` in **Company column**
   * I don't see rows without `test computer` in their **Computer name column**
   
### TODO: edit computer suite, remove computer suite, field validation suite
...
    
    
   
