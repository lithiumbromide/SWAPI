---
title: "EnableAssemblyRebuild Property (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "EnableAssemblyRebuild"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EnableAssemblyRebuild.html"
---

# EnableAssemblyRebuild Property (IAssemblyDoc)

Gets or sets whether to suspend the rebuild of the assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Property EnableAssemblyRebuild As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

instance.EnableAssemblyRebuild = value

value = instance.EnableAssemblyRebuild
```

### C#

```csharp
System.bool EnableAssemblyRebuild {get; set;}
```

### C++/CLI

```cpp
property System.bool EnableAssemblyRebuild {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to suspend rebuilding the assembly, false to rebuild the assembly (false is the default)

## VBA Syntax

See [AssemblyDoc::EnableAssemblyRebuild](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~EnableAssemblyRebuild.html).

## Examples

[Suspend Automatic Rebuilds (VBA)](Suspend_Automatic_Rebuilds_of_an_Assembly_Example_VB.htm)

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
