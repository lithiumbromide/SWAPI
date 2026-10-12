---
title: "System Options > Selection"
project: ""
interface: ""
member: ""
kind: "topic"
source: "swconst/SO_Selection.htm"
---

# System Options > Selection

| Setting | Get/Set Methods | Return Value or < Value > or < OnFlag > | Comment |
| --- | --- | --- | --- |
| Default bulk selection method - Lasso or Box | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesDefaultBulkSelection2) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesDefaultBulkSelection2, < OnFlag >) | Boolean value | True to use a lasso for bulk selection, false to use a box |
| Selection of hidden edges - Allow selection in wireframe and HLV modes | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesHiddenEdgeSelectionInWireframe) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesHiddenEdgeSelectionInWireframe, < OnFlag >) | Boolean value | Specifies whether to allow selection of hidden edges or vertices in Wireframe and Hidden Lines Visible modes |
| Selection of hidden edges - Allow selection in HLR and shaded modes | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesHiddenEdgeSelectionInHLR) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEdgesHiddenEdgeSelectionInHLR, < OnFlag >) | Boolean value | Specifies whether to allow selection of hidden edges or vertices in Wireframe and Hidden Lines Visible modes |
| Enable selection through transparency | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayEnableSelectionThroughTransparency) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swDisplayEnableSelectionThroughTransparency, < OnFlag >) | Boolean value | Specifies whether to enable selection of opaque objects behind transparent objects in graphics area or selection of nearest object regardless of transparency |
| Enhance small face selection precision | ISldWorks::GetUserPreferenceToggle (swUserPreferenceToggle_e.swEnhanceSmallFaceSelectionPrecision) ISldWorks::SetUserPreferenceToggle (swUserPreferenceToggle_e.swEnhanceSmallFaceSelectionPrecision, < OnFlag >) | Boolean value | Specifies whether to enable selecting small entities more easily |
