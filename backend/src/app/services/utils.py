from app.schemas.common.usages import UsageList
from app.schemas.enums.sanitary import SanitaryProductType, BloodLevel, CentSize


def calculate_pbac(usage_in: UsageList) -> int:
    score = 0

    if usage_in.sanitary_product == SanitaryProductType.TAMPONS:
        if usage_in.blood_level == BloodLevel.HEAVY:
            score += 10 * usage_in.times_used
        elif usage_in.blood_level == BloodLevel.MEDIUM:
            score += 5 * usage_in.times_used
        elif usage_in.blood_level == BloodLevel.LIGHT:
            score += usage_in.times_used
    elif usage_in.sanitary_product == SanitaryProductType.PADS:
        if usage_in.blood_level == BloodLevel.HEAVY:
            score += 20 * usage_in.times_used
        elif usage_in.blood_level == BloodLevel.MEDIUM:
            score += 5 * usage_in.times_used
        elif usage_in.blood_level == BloodLevel.LIGHT:
            score += usage_in.times_used
    elif usage_in.sanitary_product == SanitaryProductType.CLOTS:
        if usage_in.cent_size == CentSize.LARGE:
            score += 5 * usage_in.times_used
        elif usage_in.cent_size == CentSize.SMALL:
            score += usage_in.times_used
    elif usage_in.sanitary_product == SanitaryProductType.FLOODING:
        score += usage_in.times_used
    return score
