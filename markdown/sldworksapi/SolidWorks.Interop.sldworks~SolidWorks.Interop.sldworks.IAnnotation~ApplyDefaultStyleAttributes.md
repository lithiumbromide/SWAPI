---
title: "ApplyDefaultStyleAttributes Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "ApplyDefaultStyleAttributes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ApplyDefaultStyleAttributes.html"
---

# ApplyDefaultStyleAttributes Method (IAnnotation)

Applies the default style attribute to this annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function ApplyDefaultStyleAttributes() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim value As System.Boolean

value = instance.ApplyDefaultStyleAttributes()
```

### C#

```csharp
System.bool ApplyDefaultStyleAttributes()
```

### C++/CLI

```cpp
System.bool ApplyDefaultStyleAttributes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the operation succeeds, false if it fails

## VBA Syntax

See [Annotation::ApplyDefaultStyleAttributes](ms-its:sldworksapivb6.chm::/sldworks~Annotation~ApplyDefaultStyleAttributes.html).

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::AddOrUpdateStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~AddOrUpdateStyle.html)
[IAnnotation::DeleteStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~DeleteStyle.html)
[IAnnotation::GetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetStyleName.html)
[IAnnotation::LoadStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LoadStyle.html)
[IAnnotation::SaveStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SaveStyle.html)
[IAnnotation::SetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetStyleName.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
