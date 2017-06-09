#
# spec file for package some ceph grafana dashboards
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           grafana-dashboards-ceph
Version:        0.1
Release:        0
Summary:        Grafana dashboards to monitor a Ceph cluster
%define branch master

License:        Apache-2.0
Group:          System/Monitoring
Url:            http://bugs.opensuse.org
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  grafana
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A few dashboards for the Grafana analytics and monitoring platform that should
help to monitor a Ceph cluster.

%prep
%setup -n %name-%branch

%build

%install
install -d -m 755 %{buildroot}/var/lib/grafana/dashboards
install -m 644 ./*.json %{buildroot}/var/lib/grafana/dashboards

%files
%defattr(-,root,root,-)
%doc LICENSE
%defattr(-,grafana,grafana,-)
/var/lib/grafana/dashboards/ceph-cluster.json
/var/lib/grafana/dashboards/ceph-osd.json
/var/lib/grafana/dashboards/ceph-pools.json
/var/lib/grafana/dashboards/node.json
