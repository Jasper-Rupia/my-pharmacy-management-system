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
                <h3><i class="fa fa-user"></i> Cashier</h3>
              </div>
            </div>

            <div class="clearfix"></div>

            <div class="row">
              <div class="col-md-12 col-sm-12  ">
                <div class="x_panel">
                  <div class="x_title">
                    <h2>List of Cashiers</h2>
                    <ul class="nav navbar-right panel_toolbox">
                    <a href="add-cashier.php" class="btn btn-sm btn-info text-white"><i class="fa fa-user-plus"></i> Add Cashier</a>
                    </ul>
                    <div class="clearfix"></div>
                  </div>
                  <div class="x_content">
                  <table id="datatable" class="table table-striped table-bordered" style="width:100%">
                      <thead>
                        <tr>
                          <th>Full Name</th>
                          <th>Contact</th>
                          <th>Email</th>
                          <th>Account Status</th>
                          <th>Action</th>
                        </tr>
                      </thead>


                      <tbody>
                        <tr>
                          <td>My Name Here</td>
                          <td>+255 297 836 192</td>
                          <td>Charde1@gmail.com</td>
                          <td><span class="btn btn-sm btn-success text-white">active</span></td>
                          <td>
                              <a class="btn btn-sm btn-success text-white"><i class="fa fa-edit"></i> edit</a>
                              <a class="btn btn-sm btn-danger text-white"><i class="fa fa-trash"></i> delete</a>
                          </td>
                        </tr>
                        <tr>
                          <td>Ashton Cox</td>
                          <td>+255 674 896 521</td>
                          <td>Ashton2@gmail.com</td>
                          <td><span class="btn btn-sm btn-success text-white">active</span></td>
                          <td>
                              <a class="btn btn-sm btn-success text-white"><i class="fa fa-edit"></i> edit</a>
                              <a class="btn btn-sm btn-danger text-white"><i class="fa fa-trash"></i> delete</a>
                          </td>
                        </tr>
                        <tr>
                          <td>Cedric Lee</td>
                          <td>+255 987 686 432</td>
                          <td>Cedric3@gmail.com</td>
                          <td><span class="btn btn-sm btn-danger text-white">inactive</span></td>
                          <td>
                              <a class="btn btn-sm btn-success text-white"><i class="fa fa-edit"></i> edit</a>
                              <a class="btn btn-sm btn-danger text-white"><i class="fa fa-trash"></i> delete</a>
                          </td>
                        </tr>
                        <tr>
                          <td>John Kelly</td>
                          <td>+255 564 364 781</td>
                          <td>John4@gmail.com</td>
                          <td><span class="btn btn-sm btn-success text-white">active</span></td>
                          <td>
                              <a class="btn btn-sm btn-success text-white"><i class="fa fa-edit"></i> edit</a>
                              <a class="btn btn-sm btn-danger text-white"><i class="fa fa-trash"></i> delete</a>
                          </td>
                        </tr>
                        <tr>
                          <td>William Smith</td>
                          <td>+255 897 452 342</td>
                          <td>William@gmail.com</td>
                          <td><span class="btn btn-sm btn-danger text-white">inactive</span></td>
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
