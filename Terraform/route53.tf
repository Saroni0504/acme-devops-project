resource "aws_route53_zone" "project" {
  name = "project-roni.com"
}
resource "aws_route53_record" "cname" {
  zone_id = aws_route53_zone.project.zone_id
  name    = "www.project-roni.com"
  type    = "CNAME"
  ttl     = 300
  records = ["${aws_elb.elb.dns_name}"]
}
