---
title: "Replace Method (ISwDMComponent6)"
project: "SOLIDWORKS Document Manager API Help"
interface: "ISwDMComponent6"
member: "Replace"
kind: "method"
source: "swdocmgrapi/SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6~Replace.html"
---

# Replace Method (ISwDMComponent6)

Replace this component with the specified component.

## Syntax

### Visual Basic (Declaration)

```vb
Function Replace( _
   ByVal fileName As System.String, _
   ByVal ConfigurationName As System.String, _
   ByVal ReattachMates As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISwDMComponent6
Dim fileName As System.String
Dim ConfigurationName As System.String
Dim ReattachMates As System.Boolean
Dim value As System.Boolean

value = instance.Replace(fileName, ConfigurationName, ReattachMates)
```

### C#

```csharp
System.bool Replace(
   System.string fileName,
   System.string ConfigurationName,
   System.bool ReattachMates
)
```

### C++/CLI

```cpp
System.bool Replace(
   System.String^ fileName,
   System.String^ ConfigurationName,
   System.bool ReattachMates
)
```

### Parameters

- `fileName`: Path and file name of the component to replace this component
- `ConfigurationName`: Configuration of the component to replace this component
- `ReattachMates`: True to reattach mates to the component that replaced this component, false to not

### Return Value

True if the operation succeeds, false if it fails

## VBA Syntax

See [SwDMComponent6::Replace](ms-its:swdocmgrapivb6.chm::/swdocumentmgr~SwDMComponent6~Replace.html).

## Examples

[Replace Component (C#)](Replace_Component_Example_CSharp.htm)
[Replace Component (VB.NET)](Replace_Component_Example_VBNET.htm)

## Remarks

Call [ISwDMConfiguration11::GetReplacedComponents](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMConfiguration11~GetReplacedComponents.html) to get information about replaced components in an assembly.

**NOTE:** If you call [ISwComponent6::PathName](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6~PathName.html) after calling ISwDMComponent6::Replace and before opening and saving an assembly, then the path to the original component is returned, not the path to the replaced component. References to replaced components are not updated until the assembly is opened and saved in SOLIDWORKS.

## See Also

[ISwDMComponent6 Interface](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6.html)
[ISwDMComponent6 Members](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMComponent6_members.html)
[ISwDMDocument8::GetChangedReferences Method](SolidWorks.Interop.swdocumentmgr~SolidWorks.Interop.swdocumentmgr.ISwDMDocument8~GetChangedReferences.html)

## Availability

SOLIDWORKS Document Manager API 2009 SP0
