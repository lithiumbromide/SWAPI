---
title: "GetActiveAnnotationView Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetActiveAnnotationView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetActiveAnnotationView.html"
---

# GetActiveAnnotationView Method (IModelDocExtension)

Gets the active annotation view of this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetActiveAnnotationView() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.GetActiveAnnotationView()
```

### C#

```csharp
System.object GetActiveAnnotationView()
```

### C++/CLI

```cpp
System.Object^ GetActiveAnnotationView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IAnnotationView](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotationView.html)

## VBA Syntax

See [ModelDocExtension::GetActiveAnnotationView](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetActiveAnnotationView.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2023 SP03, Revision Number 31.3
