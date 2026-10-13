---
title: "IPropertyManagerPage2Handler9 Interface"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IPropertyManagerPage2Handler9"
member: ""
kind: "interface"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9.html"
---

# IPropertyManagerPage2Handler9 Interface

Must be implemented by the add-in application to handle callbacks from [IPropertyManagerPage2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2.html).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPropertyManagerPage2Handler9
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2Handler9
```

### C#

```csharp
public interface IPropertyManagerPage2Handler9
```

### C++/CLI

```cpp
public interface class IPropertyManagerPage2Handler9
```

## VBA Syntax

See [PropertyManagerPage2Handler9](ms-its:swpublishedapivb6.chm::/swpublished~PropertyManagerPage2Handler9.html).

## Examples

To create a SOLIDWORKS .NET add-in that implements this interface, open in Visual Studio one of these projects:

- Visual Basic - SwVBAddin
- Visual C# - SwCSharpAddin

## Examples

[Create PropertyManager Page (VBA)](Create_PropertyManager_Page_Example_VB.htm)

## Remarks

To use this interface:

- In a SOLIDWORKS VBA macro, you must reference the SOLIDWORKS exposed type libraries for add-in use type library specific to the [version of SOLIDWORKS](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~VersionHistory.html) that you are running.
- In a SOLIDWORKS VB.NET or C# add-in, you must reference the **SOLIDWORKS.interop.swpublished** assembly and set ComVisibleAttribute to true (see [ComVisibleAttribute in VB.NET or C# Macros and Add-ins](sldworksapiprogguide.chm::/OVERVIEW/ComVisibleAttribute_in_VSTA_macros.htm)).

For all unimplemented methods of this object, the add-in application can return E_NOTIMPL.

## See Also

[IPropertyManagerPage2Handler9 Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IPropertyManagerPage2Handler9_members.html)
[SolidWorks.Interop.swpublished Namespace](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished_namespace.html)
