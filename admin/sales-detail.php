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
                <h3><i class="fa fa-desktop"></i> Sales Details</h3>
              </div>
            </div>

            <div class="clearfix"></div>

            <div class="row">
              <div class="col-md-12 col-sm-12  ">
                <div class="x_panel">
                  <div class="x_title">
                    <h2><strong>SLS-101-21</strong> <small class="text-success">Nov 5, 2021</small></h2>
                    <ul class="nav navbar-right panel_toolbox">
                    <a href="#" class="btn btn-sm btn-info text-white"><i class="fa fa-plus"></i> Add Sales</a>
                    </ul>
                    <div class="clearfix"></div>
                  </div>
                  <div class="x_content">
                  <table id="datatable" class="table table-striped table-bordered" style="width:100%">
                      <thead>
                        <tr>
                          <th>Medicine Name</th>
                          <th>Quantity</th>
                          <th>Price</th>
                          <th>Total Amount</th>
                          <th>Action</th>
                        </tr>
                      </thead>


                      <tbody>
                        <tr>
                          <td>Biogesic</td>
                          <td>30</td>
                          <td>Php7.00</td>
                          <td>Php210.00</td>
                          <td>
                              <a class="btn btn-sm btn-success text-white"><i class="fa fa-edit"></i> edit</a>
                              <a class="btn btn-sm btn-danger text-white"><i class="fa fa-trash"></i> delete</a>
                          </td>
                        </tr>
                        <tr>
                          <td>Alaxan</td>
                          <td>20</td>
                          <td>Php10.00</td>
                          <td>Php200.00</td>
                          <td>
                              <a class="btn btn-sm btn-success text-white"><i class="fa fa-edit"></i> edit</a>
                              <a class="btn btn-sm btn-danger text-white"><i class="fa fa-trash"></i> delete</a>
                          </td>
                        </tr>
                        <tr>
                          <td>Tuseran</td>
                          <td>50</td>
                          <td>Php8.00</td>
                          <td>Ph400.00</td>
                          <td>
                              <a class="btn btn-sm btn-success text-white"><i class="fa fa-edit"></i> edit</a>
                              <a class="btn btn-sm btn-danger text-white"><i class="fa fa-trash"></i> delete</a>
                          </td>
                        </tr>
                        <tr>
                          <td>BioFlu</td>
                          <td>45</td>
                          <td>Php12.00</td>
                          <td>Php540.00</td>
                          <td>
                              <a class="btn btn-sm btn-success text-white"><i class="fa fa-edit"></i> edit</a>
                              <a class="btn btn-sm btn-danger text-white"><i class="fa fa-trash"></i> delete</a>
                          </td>
                        </tr>
                        <tr>
                          <td>Enervon</td>
                          <td>100</td>
                          <td>Php6.00</td>
                          <td>Php600.00</td>
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
