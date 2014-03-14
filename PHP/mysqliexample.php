<?php
try {
  $con=new MySQLi("localhost","test","test","test");
  $stmt=$con->prepare("SELECT * FROM test WHERE id = ?");
  $id=$_GET["id"];
  $stmt->bind_param("i",$id);
  $stmt->execute();
  $result=$stmt->get_result();
  foreach ($result as $row) {
    var_export($row);
  }       
} finally {
  if (isset($result)) { $result->free(); }
  if (isset($stmt)) { $stmt->close(); }
  if (isset($con)) { $con->close(); }
}
