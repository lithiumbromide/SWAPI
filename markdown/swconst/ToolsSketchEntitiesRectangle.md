---
title: "Tools > Sketch Entities > Corner Rectangle or Center Rectangle or 3 Point Corner Rectangle or 3 Point Center Rectangle or Parallelogram"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/ToolsSketchEntitiesRectangle.htm"
---

# Tools > Sketch Entities > Corner Rectangle or Center Rectangle or 3 Point Corner Rectangle or 3 Point Center Rectangle or Parallelogram

| Setting | Get/Set Methods | Return Value or < OnFlag > | Comments |
| --- | --- | --- | --- |
| Rectangle Type - Add construction lines - From Corner | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, <OnFlag> ) | Boolean value | Specifies whether to add construction lines from the corners |
| Rectangle Type - Add construction lines - From Midpoint | IModelDocExtension::GetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchAddConstToRectEntity) IModelDocExtension::SetUserPreferenceToggle (swUserPreferenceToggle_e.swSketchAddConstToRectEntity, <OnFlag> ) | Boolean value | Specifies whether to add construction lines from the midpoint |
