use strict;
use warnings;
use Parallel::ForkManager;
use Data::Dumper qw(Dumper);

my $forks =shift or die "Usage: $0 N\n";

my @numbers = map {$_ * 2000000 } reverse 1 .. 10;
my %results;
my @start = time();
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
print "Forking up to $forks at a time\n";
my %results;

print "Forking up to $forkss at a time\n;
my $pm = Parallel::ForkManager->new($forks);

$pm->run_on_finish( sub{
        my ($pid, $exit_code, $ident, $exit_signal, $core_dump, $data_sytructure_reference) = @_;
        my $q = $data_structure_refeerence->{input};
        $results{$q} = $data_structure_reference->{result};
});

foreach my $p(@numbers){
        my $pid = $ pm ->start and next;
        my $res = calc($q);
        $pm->finish(0, {result => $res, input => $q =);
}
$pm->wait_all_children;

print Dumper \%results;
my @stop = time();