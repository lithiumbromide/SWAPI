---
title: "GetMBDSTEP242Data Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetMBDSTEP242Data"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMBDSTEP242Data.html"
---

# GetMBDSTEP242Data Method (IModelDocExtension)

Gets the SOLIDWORKS MBD STEP 242 data object.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMBDSTEP242Data() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.GetMBDSTEP242Data()
```

### C#

```csharp
System.object GetMBDSTEP242Data()
```

### C++/CLI

```cpp
System.Object^ GetMBDSTEP242Data();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IMBDSTEP242Data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.html)

## VBA Syntax

See [ModelDocExtension::GetMBDSTEP242Data](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetMBDSTEP242Data.html).

## Examples

See the IMBDSTEP242DATA example.

## Remarks

SOLIDWORKS Model Based Definition (MBD) is an integrated drawingless manufacturing solution for SOLIDWORKS.

This method requires that the SOLDWORKS MBD add-in be loaded. ([ISldWorks::LoadAddIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.html))

See the SOLIDWORKS Help for details about MBD.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2025 SP03, Revision Number 33.3
