import React from "react";

function List() {
  return (
    <span>
      {/*Put the http value from return here:*/}
      {/* this Script is the javascript widget that converts the
        blockquote.twitter-tweet elements ontp fully rendered embedded tweets.

        It is unclear if this should be with the Html returned from twitter
        or if it should be seperate here.*/}
      <script
        async
        src="//platform.twitter.com/widgets.js"
        charset="utf-8"
      ></script>
    </span>
  );
}

export default List;
