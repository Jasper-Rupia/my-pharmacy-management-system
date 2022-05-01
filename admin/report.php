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
                <h3><i class="fa fa-bar-chart"></i> Sales Report</h3>
              </div>
            </div>

            <div class="clearfix"></div>

            <div class="row">
              <div class="col-md-12 col-sm-12  ">
                <div class="x_panel">
                  <div class="x_title">
                    <h2>Sales Report Graph</h2>
                    <div class="clearfix"></div>
                  </div>
                  <div class="x_content">
              <!-- graph area -->
              <div class="col-md-4 col-sm-4">
              <table class="table table-striped table-bordered" style="width:100%">
                      <thead>
                        <tr>
                          <th>Month</th>
                          <th>Sales Amount</th>
                        </tr>
                      </thead>
                      <tbody>
                        <tr>
                          <td>January</td>
                          <td>20,000</td>
                        </tr>
                        <tr>
                          <td>February</td>
                          <td>15,000</td>
                        </tr>
                        <tr>
                          <td>March</td>
                          <td>25,000</td>
                        </tr>
                        <tr>
                          <td>April</td>
                          <td>10,000</td>
                        </tr>
                        <tr>
                          <td>May</td>
                          <td>20,000</td>
                        </tr>
                        <tr>
                          <td>June</td>
                          <td>15,000</td>
                        </tr>
                        <tr>
                          <td>July</td>
                          <td>25,000</td>
                        </tr>
                        <tr>
                          <td>August</td>
                          <td>10,000</td>
                        </tr>
                        <tr>
                          <td>September</td>
                          <td>20,000</td>
                        </tr>
                        <tr>
                          <td>October</td>
                          <td>15,000</td>
                        </tr>
                        <tr>
                          <td>November</td>
                          <td>25,000</td>
                        </tr>
                        <tr>
                          <td>December</td>
                          <td>10,000</td>
                        </tr>
                        <tr>
                          <td><strong>Total</strong></td>
                          <td><strong>210,000</strong></td>
                        </tr>
                      </tbody>
                    </table>
              </div>
              
              <div class="col-md-8 col-sm-8  ">
                <div class="x_panel">
                  <div class="x_title">
                    <h2>Sales Amount</h2>
                    
                    <div class="clearfix"></div>
                  </div>
                  <div class="x_content">
                    <canvas id="lineChart"></canvas>
                  </div>
                </div>
              </div>
              <!-- /graph area -->
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <?php include 'include/footer.php';?></script>
   
  </body>
</html>
