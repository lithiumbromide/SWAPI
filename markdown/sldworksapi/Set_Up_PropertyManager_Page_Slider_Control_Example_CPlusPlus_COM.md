---
title: "Set Up PropertyManager Page Slider Control Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Up_PropertyManager_Page_Slider_Control_Example_CPlusPlus_COM.htm"
---

# Set Up PropertyManager Page Slider Control Example (C++ COM)

The following example shows how to set up a slider control.

```vb
...
id = CONTROL_SLIDER;
controlType = swControlType_Slider;
caption = _T("");
alignment = swControlAlign_Indent;
options = swControlOptions_Visible + swControlOptions_Enabled;
tip = _T("Second trackbar");
hres = m_pSwGroup_1->IAddControl(id, controlType, caption, alignment, options, tip, &m_pSwControl_1_2);
if (m_pSwControl_1_2 != NULL)
{
IPropertyManagerPageSlider* pSlider = NULL;
HRESULT res = m_pSwControl_1_2->QueryInterface(IID_IPropertyManagerPageSlider, (LPVOID*)&pSlider);
if (pSlider != NULL)
{
res = pSlider->put_Style(swPropMgrPageSliderStyle_Vertical | swPropMgrPageSliderStyle_AutoTicks | swPropMgrPageSliderStyle_BottomLeftTicks | swPropMgrPageSliderStyle_NotifyWhileTracking);
res = pSlider->SetRange(100, 200, &boolstatus);
res = pSlider->put_Position(125);
res = pSlider->put_LineSize(2);
res = pSlider->put_PageSize(10);
res = pSlider->put_Height(250);

pSlider->Release();
}
}
...
```
