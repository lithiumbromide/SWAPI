---
title: "GetReplacedComponents Method (ISwDMConfiguration11)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMConfiguration11"
member: "GetReplacedComponents"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~GetReplacedComponents.html"
---

# GetReplacedComponents Method (ISwDMConfiguration11)

Gets information about the components that were replaced by [ISwDMComponent6::Replace](SOLIDWORKS.Interop.swdocumentmgr~SOLIDWORKS.Interop.swdocumentmgr.ISwDMComponent6~Replace.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetReplacedComponents( _
   ByRef ComponentNames As System.Object, _
   ByRef ConfigurationNames As System.Object, _
   ByRef NewFilenames As System.Object, _
   ByRef MatesReattached As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMConfiguration11
Dim ComponentNames As System.Object
Dim ConfigurationNames As System.Object
Dim NewFilenames As System.Object
Dim MatesReattached As System.Object

instance.GetReplacedComponents(ComponentNames, ConfigurationNames, NewFilenames, MatesReattached)
```

### C#

```csharp
void GetReplacedComponents(
   out System.object ComponentNames,
   out System.object ConfigurationNames,
   out System.object NewFilenames,
   out System.object MatesReattached
)
```

### C++/CLI

```cpp
void GetReplacedComponents(
   [Out] System.Object^ ComponentNames,
   [Out] System.Object^ ConfigurationNames,
   [Out] System.Object^ NewFilenames,
   [Out] System.Object^ MatesReattached
)
```

### Parameters

- `ComponentNames`: Array of component names that were replaced
- `ConfigurationNames`: Array of configuration names for the components that were replaced in the document
- `NewFilenames`: Array of the path and filenames of the components that were replaced
- `MatesReattached`: Array of Booleans indicating whether the mates for the components that were replaced were reattached

## VBA Syntax

See [SwDMConfiguration11::GetReplacedComponents](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMConfiguration11~GetReplacedComponents.html).

## See Also

[ISwDMConfiguration11 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11.html)
[ISwDMConfiguration11 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11_members.html)
[ISwDMDocument8::GetChangedReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
