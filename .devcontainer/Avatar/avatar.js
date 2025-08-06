const AVATAR_CONFIG = {
  canvas: {
    width: 280,
    height: 420,
    backgroundAlpha: 0
  },
  model: {
    originalWidth: 1000,
    originalHeight: 1000,
    baseScale: 0.8,
    position: {
      x: -250,
      y: -260
    },
    scaleReduction: 0.9
  },
  motion: {
    idle: "Idle",
    flickUp: "FlickUp",
    tap: "Tap",
    flickDown: "FlickDown",
    raiseArms: "RaiseArms"
  }
};

const app = new PIXI.Application({
  view: document.getElementById("avatar"),
  autoStart: true,
  backgroundAlpha: AVATAR_CONFIG.canvas.backgroundAlpha,
  width: AVATAR_CONFIG.canvas.width,
  height: AVATAR_CONFIG.canvas.height,
  resolution: window.devicePixelRatio || 1
});

let model;

const setupModel = () => {
  if (!model) return;
  const { originalWidth, originalHeight, baseScale, scaleReduction, position } = AVATAR_CONFIG.model;
  const { width: targetWidth, height: targetHeight } = app.screen;
  const scaleX = (targetWidth / originalWidth) * baseScale;
  const scaleY = (targetHeight / originalHeight) * baseScale;
  const scale = Math.min(scaleX, scaleY) * scaleReduction;
  model.scale.set(scale, scale);
  model.x = (targetWidth / 2) + position.x;
  model.y = (targetHeight / 2) + position.y;
};

const handleMouseMove = (e) => {
  if (!model?.internalModel) return;
  const rect = app.view.getBoundingClientRect();
  const x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
  const y = ((e.clientY - rect.top) / rect.height) * 2 - 1;
  model.internalModel.coreModel.setParameterValueById("ParamAngleX", x * 30);
  model.internalModel.coreModel.setParameterValueById("ParamAngleY", y * 30);
  model.internalModel.coreModel.setParameterValueById("ParamEyeBallX", x);
  model.internalModel.coreModel.setParameterValueById("ParamEyeBallY", y);
};

const startMotion = (motionName) => {
  if (!model?.internalModel) return;
  model.internalModel.motionManager.stopAllMotions();
  model.motion(motionName);
};

PIXI.live2d.Live2DModel.from("assets/Haru/mark_free_en/runtime/mark_free_t04.model3.json")
  .then((loadedModel) => {
    model = loadedModel;
    app.stage.addChild(model);
    setupModel();
    startMotion(AVATAR_CONFIG.motion.idle);
    window.addEventListener("mousemove", handleMouseMove);
  })
  .catch(console.error);

document.getElementById("actionsFlickUp").addEventListener("click", () => startMotion(AVATAR_CONFIG.motion.flickUp));
document.getElementById("actionsTap").addEventListener("click", () => startMotion(AVATAR_CONFIG.motion.tap));
document.getElementById("actionsFlickDown").addEventListener("click", () => startMotion(AVATAR_CONFIG.motion.flickDown));
document.getElementById("actionsRaiseArms").addEventListener("click", () => startMotion(AVATAR_CONFIG.motion.raiseArms));