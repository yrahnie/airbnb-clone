const gulp = require("gulp");

// 이 파일은 기본적으로 SASS 코드를 가져다가 CSS 코드로 만듬.
// assts/scss/styles.scss 파일을 수정해야 하고 이를 npm run css 실행해서 static/css/styles.css 에 반영되도록 한 후 이를 올려야함.
const css = () => {
  const postCSS = require("gulp-postcss");
  const sass = require("gulp-sass")(require("sass"));
  const minify = require("gulp-csso");
  sass.compiler = require("node-sass");
  return gulp
    .src("assets/scss/styles.scss") // assets/scss/styles.scss 파일을 가져와서
    .pipe(sass().on("error", sass.logError)) // css 파일로 바꿈.
    .pipe(postCSS([require("tailwindcss"), require("autoprefixer")])) // 모든 tailwind 내용을 가져다가 real css 로 만들어줌
    .pipe(minify()) // 작게 만들어줌
    .pipe(gulp.dest("static/css")); // 결과를 static/css 폴더로 보냄
};

exports.default = css;
