---
title: "ResetStandardViews Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "ResetStandardViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ResetStandardViews.html"
---

# ResetStandardViews Method (IModelDocExtension)

Returns all standard model views to their default settings.

## Syntax

### Visual Basic (Declaration)

```vb
Function ResetStandardViews() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.ResetStandardViews()
```

### C#

```csharp
System.bool ResetStandardViews()
```

### C++/CLI

```cpp
System.bool ResetStandardViews();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True to return all standard model views to their default settings, false to not

## VBA Syntax

See [ModelDocExtension::ResetStandardViews](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~ResetStandardViews.html).

## Remarks

This method works with parts and assemblies only.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::UpdateStandardViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateStandardViews.html)
[IModelDoc2::ShowNamedView2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowNamedView2.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
