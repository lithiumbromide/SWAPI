---
title: "GetSmartArrowHeadStyle Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "GetSmartArrowHeadStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetSmartArrowHeadStyle.html"
---

# GetSmartArrowHeadStyle Method (IAnnotation)

Gets the setting for smart arrowhead style for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSmartArrowHeadStyle() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Boolean

value = instance.GetSmartArrowHeadStyle()
```

### C#

```csharp
System.bool GetSmartArrowHeadStyle()
```

### C++/CLI

```cpp
System.bool GetSmartArrowHeadStyle();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the smart arrowhead style setting is enabled, false if the smart arrowhead style setting is disabled

## VBA Syntax

See [Annotation::GetSmartArrowHeadStyle](ms-its:sldworksapivb6.chm::/sldworks~Annotation~GetSmartArrowHeadStyle.html).

## Remarks

The smart arrowhead style flag is a characteristic of the annotation, not individual leaders. You can get or set it whether or not leaders are currently displayed.

| Use... | To... |
| --- | --- |
| IAnnotation::GetLeaderStyle | Get leader characteristics |
| IAnnotation::SetLeader3 | Set leader characteristics |

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
