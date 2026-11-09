from robojudo.config import cfg_registry
from robojudo.controller.ctrl_cfgs import (
    JoystickCtrlCfg,  # noqa: F401
    KeyboardCtrlCfg,  # noqa: F401
    UnitreeCtrlCfg,  # noqa: F401
)
from robojudo.pipeline.pipeline_cfgs import (
    RlLocoMimicPipelineCfg,  # noqa: F401
    RlMultiPolicyPipelineCfg,  # noqa: F401
    RlPipelineCfg,  # noqa: F401
)

from .ctrl.g1_beyondmimic_ctrl_cfg import G1BeyondmimicCtrlCfg  # noqa: F401
from .ctrl.g1_motion_ctrl_cfg import (  # noqa: F401
    G1MotionCtrlCfg,
    G1MotionH2HCtrlCfg,
    G1MotionKungfuBotCtrlCfg,
    G1MotionTwistCtrlCfg,
)
from .ctrl.g1_twist_redis_ctrl_cfg import G1TwistRedisCtrlCfg  # noqa: F401
from .env.g1_dummy_env_cfg import G1DummyEnvCfg  # noqa: F401
from .env.g1_mujuco_env_cfg import G1_12MujocoEnvCfg, G1_23MujocoEnvCfg, G1MujocoEnvCfg  # noqa: F401
from .env.g1_real_env_cfg import G1RealEnvCfg, G1UnitreeCfg  # noqa: F401
from .policy.g1_amo_policy_cfg import G1AmoPolicyCfg  # noqa: F401
from .policy.g1_asap_policy_cfg import G1AsapLocoPolicyCfg, G1AsapPolicyCfg  # noqa: F401
from .policy.g1_beyondmimic_policy_cfg import G1BeyondMimicPolicyCfg  # noqa: F401
from .policy.g1_h2h_policy_cfg import G1H2HPolicyCfg  # noqa: F401
from .policy.g1_kungfubot_policy_cfg import G1KungfuBotGeneralPolicyCfg, G1KungfuBotPolicyCfg  # noqa: F401
from .policy.g1_smooth_policy_cfg import G1SmoothPolicyCfg  # noqa: F401
from .policy.g1_twist_policy_cfg import G1TwistPolicyCfg  # noqa: F401
from .policy.g1_unitree_policy_cfg import G1UnitreePolicyCfg, G1UnitreeWoGaitPolicyCfg  # noqa: F401
from .policy.g1_kungfubot_policy_cfg import G1KungfuBotGeneralPolicyCfg, G1KungfuBotPolicyCfg
from .pipeline.g1_locomimic_pipeline_cfg import G1RlLocoMimicPipelineCfg
from robojudo.policy.holosoma_policy import HolosomaPolicyCfg

# ======================== Custom Configs ======================== #
"""
Add your custom config here.
"""
@cfg_registry.register
class g1_dev(G1RlLocoMimicPipelineCfg):
    """
    Example of loco mimic pipeline configuration.
    You can switch between loco and mimic policies during runtime, with interpolation.
    === Check more fancy locomimic examples in g1_loco_mimic_cfg.py ===
    """

    robot: str = "g1"
    #env: G1MujocoEnvCfg = G1MujocoEnvCfg()
    env: G1RealEnvCfg = G1RealEnvCfg(
        env_type = "UnitreeCppEnv",
        unitree=G1UnitreeCfg(
            net_if="enP7s7",
        )
    )

    ctrl: list[KeyboardCtrlCfg | JoystickCtrlCfg] = [
        JoystickCtrlCfg(
            triggers_extra={
                "A": "[POLICY_LOCO]",
                "B": "[POLICY_MIMIC]",
            }
        ),
        KeyboardCtrlCfg(
            triggers_extra={
                "]": "[POLICY_LOCO]",
                "[": "[POLICY_MIMIC]",
            }
        ),
    ]

    upper_dof_pos_default: list[float] | None = None  # keep env default (arms at 0) during loco

    loco_policy: G1UnitreePolicyCfg = G1UnitreePolicyCfg()
    mimic_policies: list[G1AsapPolicyCfg] = [
        #G1KungfuBotPolicyCfg(),
        G1BeyondMimicPolicyCfg(policy_name="Dance_wose", without_state_estimator=True, max_timestep=1500),
        #HolosomaPolicyCfg(
        #    policy_file="assets/models/g1/holosoma/gvhmr_mj_dance_model_29999.onnx",
        #    policy_name="MJDance"
        #),
        #HolosomaPolicyCfg(
        #    policy_file="assets/models/g1/holosoma/amass_dance_chacha_model_14999.onnx",
        #    policy_name="ChaChaDance"
        #),
        #HolosomaPolicyCfg(
        #    policy_file="assets/models/g1/holosoma/amass_cleaning_model_14999.onnx",
        #    policy_name="Cleaning",
        #    without_state_estimator=True
        #),
        #HolosomaPolicyCfg(
        #    policy_file="assets/models/g1/holosoma/amass_violin_model_19999.onnx",
        #    policy_name="Violin"
        #),
        #HolosomaPolicyCfg(
        #    policy_file="assets/models/g1/holosoma/amass_boxing_model_09999.onnx",
        #    policy_name="Boxing"
        #),


    ]
