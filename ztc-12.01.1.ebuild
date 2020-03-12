# Copyright 1999-2009 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Header: $

EAPI=3

inherit distutils

DESCRIPTION="Zabbix Templates Collection"
HOMEPAGE="http://trac.greenmice.info/ztc/"
SRC_URI="https://bitbucket.org/rvs/ztc/downloads/ztc-${PV}.tar.gz"

LICENSE="GPL-3"
SLOT="0"
KEYWORDS="~x86 ~amd64"
IUSE="3ware postgres mysql nginx apache2 java php fpm mongodb"

DEPEND="
	>=dev-lang/python-2.4
	sys-apps/smartmontools
	sys-apps/lm_sensors
	postgres? (
		>=dev-db/postgresql-server-8.3
		dev-python/psycopg
	)
	mysql? (
		dev-python/mysql-python
		>=dev-db/mysql-5.0
	)
    nginx? (                                                                                                                                                 
	        www-servers/nginx[nginx_modules_http_stub_status]
	)
	apache2? (
		www-servers/apache[apache2_modules_status]
	)
	3ware? (
		sys-block/tw_cli
	)
    php? ( dev-lang/php                                                                                                                                      
		fpm? ( dev-lang/php[fpm] )
	)
	java? ( virtual/jre )
    mongodb? (
		dev-db/mongodb
        dev-python/pymongo
	)

	net-analyzer/zabbix[agent]
"
RDEPEND="$DEPEND"

src_prepare() {
	cd ztc
	#distutils_src_prepare
}

src_compile() {
	cd ztc
	distutils_src_compile
}

src_install() {
	cd ztc
	distutils_src_install
	dodoc README
	dodoc REQUIREMENTS
}
