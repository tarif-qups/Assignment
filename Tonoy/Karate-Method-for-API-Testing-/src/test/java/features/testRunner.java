package features;

import com.intuit.karate.junit5.Karate;

class TestRunner {

    @Karate.Test
    Karate Getreq() {
        return Karate.run("get_user").relativeTo(getClass());
    }

    @Karate.Test
    Karate Postreq() {
        return Karate.run("post_user").relativeTo(getClass());
    }


    @Karate.Test
    Karate Putreq() {
        return Karate.run("put_user").relativeTo(getClass());
    }

    @Karate.Test
    Karate Patchreq() {
        return Karate.run("patch_user").relativeTo(getClass());
    }

    @Karate.Test
    Karate Deletereq() {
        return Karate.run("delete").relativeTo(getClass());
    }

}
