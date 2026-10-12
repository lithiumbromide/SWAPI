---
title: "ComponentReload2 Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "ComponentReload2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ComponentReload2.html"
---

# ComponentReload2 Method (IAssemblyDoc)

Reloads and/or sets the read-only state of the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
Function ComponentReload2( _
   ByVal Component As System.Object, _
   ByVal ReadOnly As System.Boolean, _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Component As System.Object
Dim ReadOnly As System.Boolean
Dim Options As System.Integer
Dim value As System.Integer

value = instance.ComponentReload2(Component, ReadOnly, Options)
```

### C#

```csharp
System.int ComponentReload2(
   System.object Component,
   System.bool ReadOnly,
   System.int Options
)
```

### C++/CLI

```cpp
System.int ComponentReload2(
   System.Object^ Component,
   System.bool ReadOnly,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Component`: [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.html)
- `ReadOnly`: True to set Component read-only after reload, false to allow write access
- `Options`: Reload option as defined by [swComponentReloadOption_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentReloadOption_e.html)

### Return Value

Error code as defined by [swComponentReloadError_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentReloadError_e.html)

## VBA Syntax

See [AssemblyDoc::ComponentReload2](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~ComponentReload2.html).

## Examples

'VBA

'Preconditions:

'1. Open `public_documents`**\SOLIDWORKS\SOLIDWORKS 2021\samples\tutorial\api\arm2.sldasm**.

'2. Open the Immediate window.

'Postconditions:

' Inspect the Immediate window.

'=============================================

Dim swApp As SldWorks.SldWorks
Dim SWMODEL As SldWorks.ModelDoc2
Dim SWASSY As SldWorks.AssemblyDoc
Dim swcomponent As SldWorks.Component2
Dim Error As swComponentReloadError_e
Option Explicit
Sub main()
Set swApp = Application.SldWorks
Set SWMODEL = swApp.ActiveDoc
Set SWASSY = SWMODEL
Set swcomponent = SWASSY.GetComponentByName("secondgrip-1")
Debug.Print swcomponent.GetPathName
Error = SWASSY.**ComponentReload2**(swcomponent, True, swComponentReloadOption_e.swDontReloadOldComponents)
Debug.Print "Error code: " & Error
End Sub

## Remarks

This method is analogous to the Reload dialog that appears when you right-click on an assembly component in the FeatureManager design tree and select **Reload**. For more information, read the **SOLIDWORKS Design user-interface Help > Fundamentals > Document Basics > Multi-User Environment > Reload** topic.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IAssemblyDoc::ReplaceComponents2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents2.html)
[IModelDoc2::ReloadOrReplace Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ReloadOrReplace.html)

## Availability

SOLIDWORKS 2001Plus
