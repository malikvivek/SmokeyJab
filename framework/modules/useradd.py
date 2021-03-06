try:
    from framework.main import ModuleBase
except ImportError:
    pass

class UserAdd(ModuleBase):
    @property
    def needs_root(self):
        return True

    @property
    def relative_delay(self):
        return 90

    @property
    def absolute_duration(self):
        return 24 * 3600  # 1 day

    def run(self):
        self.start()
        import time
        from subprocess import check_call, PIPE
        username = 'testuser'
        cmd = 'useradd -M -c "RedTeam Test User" -l -N -s /bin/false {0}'.format(username)
        try:
            check_call(cmd, shell=True, stdout=PIPE, stderr=PIPE)
            self.hec_logger('Added a user', username=username)
        except Exception as e:
            self.hec_logger(str(e), severity='error')
            self.finish()
            return
        time.sleep(self.absolute_duration)
        try:
            check_call('userdel {0}'.format(username), shell=True, stdout=PIPE, stderr=PIPE)
            self.hec_logger('Removed a user', username=username)
        except Exception as e:
            self.hec_logger(str(e), severity='error')
        self.finish()
