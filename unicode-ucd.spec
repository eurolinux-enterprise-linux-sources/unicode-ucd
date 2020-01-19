# for other future directories from http://www.unicode.org/Public
%global unicodedir %{_datadir}/unicode
%global ucddir %{unicodedir}/ucd

Name:           unicode-ucd
Version:        6.3.0
Release:        1%{?dist}
Summary:        Unicode Character Database

# https://fedoraproject.org/wiki/Licensing/MIT#Modern_Style_without_sublicense_.28Unicode.29
License:        MIT
URL:            http://www.unicode.org/ucd/
Source0:        http://www.unicode.org/Public/zipped/%{version}/UCD.zip
# http://www.unicode.org/terms_of_use.html referenced in ReadMe.txt redirects to:
Source1:        http://www.unicode.org/copyright.html
BuildArch:      noarch

%description
The Unicode Character Database (UCD) consists of a number of data files listing
Unicode character properties and related data. It also includes data files
containing test data for conformance to several important Unicode algorithms.


%prep
%setup -q -c

grep -q "%{version}" ReadMe.txt || (echo "zip file seems not %{version}" ; exit 1)

# license terms for doc
cp -p %{SOURCE1} .


%build
%{nil}


%install
mkdir -p %{buildroot}%{ucddir}
cp -ar . %{buildroot}%{ucddir}


%files
%doc copyright.html
%dir %{unicodedir}
%{ucddir}


%changelog
* Tue Oct  8 2013 Jens Petersen <petersen@redhat.com> - 6.3.0-1
- update to 6.3 (#1013930)
- add a version check to prevent packaging a version mismatch

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Oct 24 2012 Jens Petersen <petersen@redhat.com> - 6.2.0-3
- do not use macro in comment

* Wed Oct 24 2012 Jens Petersen <petersen@redhat.com> - 6.2.0-2
- update to latest copyright file from the website

* Wed Sep 26 2012 Jens Petersen <petersen@redhat.com> - 6.2.0-1
- update to Unicode 6.2

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar  2 2012 Jens Petersen <petersen@redhat.com> - 6.1.0-1
- update to Unicode 6.1

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Jens Petersen <petersen@redhat.com> - 6.0.0-3
- do not duplicate ReadMe.txt in doc files

* Tue Nov 29 2011 Jens Petersen <petersen@redhat.com> - 6.0.0-2
- fix duplicate copyright file (#757290)
- drop superfluous BR on unzip

* Sat Nov 26 2011 Jens Petersen <petersen@redhat.com> - 6.0.0-1
- package Unicode 6.0 UCD
- MIT license
