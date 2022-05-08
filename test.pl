#! /usr/bin/env perl

use strict;
use warnings;
use Data::Dumper qw(Dumper);

my $start = time();

my @numbers = map { $_ * 2000000 } reverse 1 .. 10;
my %results;

foreach my $q (@numbers) {
    $results{$q} = calc($q);
}

print Dumper \%results;

my $stop = time();
my $temps = $stop - $start;

print "Temps de calcul: $temps secondes \n";

sub calc {
    my ($n) = @_;
    my $sum = 0;
    for (1 .. $n) {
        $sum += 1 + rand()/100;
    }
    return $sum;
}