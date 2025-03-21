firewall {
    family inet {
        /*
         ** $Id:$
         ** $Date:$
         ** $Revision:$
         **
         ** Juniper policy for overlap case.
         */
        replace: filter SamplePolicy {
            interface-specific;
            term accept-web-services {
                from {
                    source-address {
                        1.2.3.0/24;
                    }
                    destination-port [ 80 443 ];
                    protocol tcp;
                }
                then accept;
            }
            term accept-ssh {
                from {
                    source-address {
                        1.2.0.0/16;
                    }
                    destination-port 22;
                    protocol tcp;
                }
                then accept;
            }
            term accept-mysql {
                from {
                    source-address {
                        1.0.0.0/8;
                        8.8.8.8/32;
                    }
                    destination-port 3306;
                    protocol tcp;
                }
                then accept;
            }
        }
    }
}
