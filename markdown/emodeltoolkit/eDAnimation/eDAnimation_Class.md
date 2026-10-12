---
title: "eDAnimation Class"
project: ""
interface: "eDAnimation"
member: ""
kind: "class"
source: "emodeltoolkit/eDAnimation/eDAnimation_Class.htm"
---

# eDAnimation Class

| See Also | Example | Accessors | Availability |
| --- | --- | --- | --- |

Contains either an animation sequence or a set of explode steps. See also [eDConfiguration::CreateAnimation](../eDConfiguration/eDConfiguration_Class.htm) and [eDConfiguration::CreateExplode](../eDConfiguration/eDConfiguration_Class.htm).

#### Header file code

```vb
class eDAnimation : public eDObject

public:

eDOutcome CreateComponentAnimation( const eDPart *part, double starttime, double duration, const eDTransform3d &transform ); //Create animation

eDOutcome CreateExplodeStep( const eDPart *part, const eDTransform3d &transform ); //Create explode steps
};
```
