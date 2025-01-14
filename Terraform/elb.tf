resource "aws_elb" "elb" {
  name               = "elb"
  availability_zones = ["us-east-1a", "us-east-1b"]
  listener {
    instance_port     = 80
    instance_protocol = "HTTP"
    lb_port           = 80
    lb_protocol       = "HTTP"
  }
  listener {
    instance_port     = 443
    instance_protocol = "TCP"  # TODO: When there will be a ssl certificate change to HTTPS
    lb_port           = 443
    lb_protocol       = "TCP"  # TODO: When there will be a ssl certificate change to HTTPS
  }
  health_check {
    target              = "HTTP:80/"
    interval            = 30
    timeout             = 5
    unhealthy_threshold = 2
    healthy_threshold   = 2
  }
  cross_zone_load_balancing = true
  tags = {
    Name = "elb"
  }
}
