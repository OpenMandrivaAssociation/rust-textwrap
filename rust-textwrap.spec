# Tests disabled to avoid circular dependency (criterion)
%bcond_with check
%global debug_package %{nil}

%global crate textwrap

Name:           rust-%{crate}
Version:        0.13.4
Release:        2
Summary:        Small library for word wrapping, indenting, and dedenting strings

# Upstream license specification: MIT
License:        MIT
URL:            https://crates.io/crates/textwrap
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Small library for word wrapping, indenting, and dedenting strings.

You can use it to format strings (such as help and error messages) for display
in commandline applications. It is designed to be efficient and handle Unicode
characters correctly.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+hyphenation-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+hyphenation-devel %{_description}

This package contains library source intended for building other packages
which use "hyphenation" feature of "%{crate}" crate.

%files       -n %{name}+hyphenation-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%package     -n %{name}+term_size-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+term_size-devel %{_description}

This package contains library source intended for building other packages
which use "term_size" feature of "%{crate}" crate.

%files       -n %{name}+term_size-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
