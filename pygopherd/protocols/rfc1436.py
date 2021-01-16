from pygopherd.protocols.base import BaseGopherProtocol


class GopherProtocol(BaseGopherProtocol):
    """Implementation of basic protocol.  Will handle every query."""

    def canhandlerequest(self):
        if len(self.requestlist) > 1:
            self.searchrequest = self.requestlist[1]
        return 1

    def renderobjinfo(self, entry):
        retval = (
            entry.gettype("0")
            + entry.getname()
            + "\t"
            + entry.getselector()
            + "\t"
            + entry.gethost(default=self.server.server_name)
            + "\t"
            + str(entry.getport(default=self.server.server_port))
        )
        if entry.getgopherpsupport():
            return retval + "\t+\r\n"
        else:
            return retval + "\r\n"
