---
title: "SaveStyle Method (IAnnotation)"
project: "SOLIDWORKS API Help"
interface: "IAnnotation"
member: "SaveStyle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SaveStyle.html"
---

# SaveStyle Method (IAnnotation)

Saves the specified style.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveStyle( _
   ByVal StyleName As System.String, _
   ByVal PathName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAnnotation
Dim StyleName As System.String
Dim PathName As System.String
Dim value As System.Boolean

value = instance.SaveStyle(StyleName, PathName)
```

### C#

```csharp
System.bool SaveStyle(
   System.string StyleName,
   System.string PathName
)
```

### C++/CLI

```cpp
System.bool SaveStyle(
   System.String^ StyleName,
   System.String^ PathName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `StyleName`: Name of the style
- `PathName`: Path and filename to which to save the style

## VBA Syntax

See [Annotation::SaveStyle](ms-its:sldworksapivb6.chm::/sldworks~Annotation~SaveStyle.html).

## Remarks

See SOLIDWORKS Help for the filename extensions to use for styles.

## See Also

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.html)
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.html)
[IAnnotation::AddOrUpdateStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~AddOrUpdateStyle.html)
[IAnnotation::ApplyDefaultStyleAttributes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~ApplyDefaultStyleAttributes.html)
[IAnnotation::DeleteStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~DeleteStyle.html)
[IAnnotation::GetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetStyleName.html)
[IAnnotation::LoadStyle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~LoadStyle.html)
[IAnnotation::SetStyleName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetStyleName.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
