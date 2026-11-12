---
title: "SetStyleName Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "SetStyleName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetStyleName.html"
---

# SetStyleName Method (IAnnotation)

Sets the style for this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetStyleName( _
   ByVal StyleName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim StyleName As System.String
Dim value As System.Boolean

value = instance.SetStyleName(StyleName)
```

### C#

```csharp
System.bool SetStyleName(
   System.string StyleName
)
```

### C++/CLI

```cpp
System.bool SetStyleName(
   System.String^ StyleName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StyleName`: Name of the style

### Return Value

True if the style is set, false if not

## VBA Syntax

See [Annotation::SetStyleName](ms-its:sldworksapivb6.chm::/sldworks~Annotation~SetStyleName.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::AddOrUpdateStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~AddOrUpdateStyle.html)
[IAnnotation::ApplyDefaultStyleAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ApplyDefaultStyleAttributes.html)
[IAnnotation::DeleteStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~DeleteStyle.html)
[IAnnotation::GetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetStyleName.html)
[IAnnotation::LoadStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LoadStyle.html)
[IAnnotation::SaveStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SaveStyle.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
