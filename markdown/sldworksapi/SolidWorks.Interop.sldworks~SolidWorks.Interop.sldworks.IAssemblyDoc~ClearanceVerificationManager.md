---
title: "ClearanceVerificationManager Property (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ClearanceVerificationManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ClearanceVerificationManager.html"
---

# ClearanceVerificationManager Property (IAssemblyDoc)

Gets the clearance verification manager.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ClearanceVerificationManager As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Object

value = instance.ClearanceVerificationManager
```

### C#

```csharp
System.object ClearanceVerificationManager {get;}
```

### C++/CLI

```cpp
property System.Object^ ClearanceVerificationManager {
   System.Object^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

[IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html)

## VBA Syntax

See [AssemblyDoc::ClearanceVerificationManager](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ClearanceVerificationManager.html).

## Examples

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.html) examples.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IClearanceResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult.html)

## Availability

SOLIDWORKS 2024 SP01, Revision Number 32.1
