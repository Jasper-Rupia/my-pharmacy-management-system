<!DOCTYPE html>
<html lang="en">
<?php include 'include/header.php';?>

  <body class="nav-md">
            <?php include 'include/sidebar.php';?>
            <?php include 'include/menufooter.php';?>
          </div>
        </div>

        <?php include 'include/topnav.php';?>

        <!-- page content -->
        <div class="right_col" role="main">
          <div class="">
            <div class="page-title">
              <div class="title_left">
                <h3><i class="fa fa-truck"></i> Supplier</h3>
              </div>
            </div>

            <div class="clearfix"></div>

            <div class="row">
              <div class="col-md-12 col-sm-12  ">
                <div class="x_panel">
                  <div class="x_title">
                    <h2>List of Suppliers</h2>
                    <ul class="nav navbar-right panel_toolbox">
                    <a href="add-supplier.php" class="btn btn-sm btn-info text-white"><i class="fa fa-plus"></i> Add Supplier</a>
                    </ul>
                    <div class="clearfix"></div>
                  </div>
                  <div class="x_content">
                  <table id="datatable" class="table table-striped table-bordered" style="width:100%">
                      <thead>
                        <tr>
                          <th>Supplier Name</th>
                          <th>Contact</th>
                          <th>Email</th>
                          <th>Complete Address</th>
                          <th>Action</th>
                        </tr>
                      </thead>


                      <tbody>
                        <tr>
                          <td>Supplier 1</td>
                          <td>+255 297 837 192</td>
                          <td>supplier1@gmail.com</td>
                          <td>456 Boni Av. Moro, Tanzania</td>
                          <td>
                              <a class="btn btn-sm btn-success text-white"><i class="fa fa-edit"></i> edit</a>
                              <a class="btn btn-sm btn-danger text-white"><i class="fa fa-trash"></i> delete</a>
                          </td>
                        </tr>
                        <tr>
                          <td>Supplier 2</td>
                          <td>+255 674 897 521</td>
                          <td>supplier2@gmail.com</td>
                          <td>456 Pioneer St. Pasig, Tanzania</td>
                          <td>
                              <a class="btn btn-sm btn-success text-white"><i class="fa fa-edit"></i> edit</a>
                              <a class="btn btn-sm btn-danger text-white"><i class="fa fa-trash"></i> delete</a>
                          </td>
                        </tr>
                        <tr>
                          <td>Supplier 3</td>
                          <td>+255 987 687 432</td>
                          <td>supplier3@gmail.com</td>
                          <td>463 Boni Av. Moro, Tanzania</td>
                          <td>
                              <a class="btn btn-sm btn-success text-white"><i class="fa fa-edit"></i> edit</a>
                              <a class="btn btn-sm btn-danger text-white"><i class="fa fa-trash"></i> delete</a>
                          </td>
                        </tr>
                        <tr>
                          <td>Supplier 4</td>
                          <td>+255 564 365 781</td>
                          <td>supplier4@gmail.com</td>
                          <td>875 Pembo Makati, Tanzania</td>
                          <td>
                              <a class="btn btn-sm btn-success text-white"><i class="fa fa-edit"></i> edit</a>
                              <a class="btn btn-sm btn-danger text-white"><i class="fa fa-trash"></i> delete</a>
                          </td>
                        </tr>
                        <tr>
                          <td>Supplier 5</td>
                          <td>+255 897 454 342</td>
                          <td>supplier5@gmail.com</td>
                          <td>25 St. BGC, Tanzania</td>
                          <td>
                              <a class="btn btn-sm btn-success text-white"><i class="fa fa-edit"></i> edit</a>
                              <a class="btn btn-sm btn-danger text-white"><i class="fa fa-trash"></i> delete</a>
                          </td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <?php include 'include/footer.php';?>
  </body>
</html>
