resource "aws_route53_zone" "acme" {
  name = "acme-roni.com"
}
resource "aws_route53_record" "cname" {
  zone_id = aws_route53_zone.acme.zone_id
  name    = "www.acme-roni.com"
  type    = "CNAME"
  ttl     = 300
  records = ["${aws_elb.elb_acme.dns_name}"]
}
