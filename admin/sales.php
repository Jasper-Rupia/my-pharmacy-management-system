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
                <h3><i class="fa fa-desktop"></i> Sales</h3>
              </div>
            </div>

            <div class="clearfix"></div>

            <div class="row">
              <div class="col-md-12 col-sm-12  ">
                <div class="x_panel">
                  <div class="x_title">
                    <h2>List of Sales</h2>
                    <div class="clearfix"></div>
                  </div>
                  <div class="x_content">
                  <table id="datatable" class="table table-striped table-bordered" style="width:100%">
                      <thead>
                        <tr>
                          <th>Sales No.</th>
                          <th>Date</th>
                          <th>Total Amount</th>
                          <th>Cashier</th>
                          <th>View Details</th>
                        </tr>
                      </thead>


                      <tbody>
                        <tr>
                          <td>SLS-101-21</td>
                          <td>Nov 6, 2021</td>
                          <td>Php 20,000.00</td>
                          <td>John Kelly</td>
                          <td>
                              <a href="sales-detail.php" class="btn btn-sm btn-info text-white"><i class="fa fa-eye"></i> view details</a>
                          </td>
                        </tr>
                        <tr>
                          <td>SLS-212-21</td>
                          <td>Nov 2, 2021</td>
                          <td>Php 50,000.00</td>
                          <td>William Smith</td>
                          <td>
                              <a href="sales-detail.php" class="btn btn-sm btn-info text-white"><i class="fa fa-eye"></i> view details</a>
                          </td>
                        </tr>
                        <tr>
                          <td>SLS-112-21</td>
                          <td>Nov 4, 2021</td>
                          <td>Php 30,000.00</td>
                          <td>Ashton Cox</td>
                          <td>
                              <a href="sales-detail.php" class="btn btn-sm btn-info text-white"><i class="fa fa-eye"></i> view details</a>
                          </td>
                        </tr>
                        <tr>
                          <td>SLS-456-21</td>
                          <td>Nov 5, 2021</td>
                          <td>Php 40,000.00</td>
                          <td>Cedric Lee</td>
                          <td>
                              <a href="sales-detail.php" class="btn btn-sm btn-info text-white"><i class="fa fa-eye"></i> view details</a>
                          </td>
                        </tr>
                        <tr>
                          <td>SLS-241-21</td>
                          <td>Nov 3, 2021</td>
                          <td>Php 25,000.00</td>
                          <td>William Jones</td>
                          <td>
                              <a href="sales-detail.php" class="btn btn-sm btn-info text-white"><i class="fa fa-eye"></i> view details</a>
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
