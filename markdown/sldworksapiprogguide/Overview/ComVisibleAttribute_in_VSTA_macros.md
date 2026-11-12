---
title: "ComVisibleAttribute in VB.NET and C# Macros and Add-ins"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/ComVisibleAttribute_in_VSTA_macros.htm"
---

# ComVisibleAttribute in VB.NET and C# Macros and Add-ins

VB.NET and C# macros and add-ins must specify a runtime class attribute, ComVisibleAttribute, when implementing SolidWorks.Interop.swpublished interfaces.

For example, when defining an object that implements any of the interfaces in SolidWorks.Interop.swpublished, specify the System.Runtime.InteropServices.ComVisibleAttribute class attribute on the line before the implementing class. Note the underscore character at the end of the first line of the VB.NET example.

### VB.NET

```vb
<System.Runtime.InteropServices.ComVisibleAttribute(True)> _
Public Class clsPropMgr
       Implements PropertyManagerPage2Handler7
{
```

### C#

```vb
[System.Runtime.InteropServices.ComVisibleAttribute(true)]
public class clsPropMgr : PropertyManagerPage2Handler7
{
```

Use ComVisibleAttribute in VB.NET and C# macros and add-ins that implement these interfaces:

- [IPropertyManagerPage2Handler7](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.IPropertyManagerPage2Handler7.html)
- [ISwAddin](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwAddin.html)
- [ISwAddinBroker](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwAddinBroker.html)
- [ISwCalloutHandler](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwCalloutHandler.html)
- [ISwColorContour](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwColorContour.html)
- [ISwComFeature](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwComFeature.html)
- [ISwManipulatorHandler2](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwManipulatorHandler2.html)
- [ISwQuicktip](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwQuicktip.html)
- [ISwUndoAPIHandler](swpublishedAPI.chm::/SolidWorks.interop.swpublished~SolidWorks.interop.swpublished.ISwUndoAPIHandler.html)
