---
title: "InsertEnvelope Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "InsertEnvelope"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertEnvelope.html"
---

# InsertEnvelope Method (IAssemblyDoc)

Adds an envelope in the specified configuration name in this assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertEnvelope( _
   ByVal CompName As System.String, _
   ByVal ConfigName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As Component2
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim ConfigName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As Component2

value = instance.InsertEnvelope(CompName, ConfigName, X, Y, Z)
```

### C#

```csharp
Component2 InsertEnvelope(
   System.string CompName,
   System.string ConfigName,
   System.double X,
   System.double Y,
   System.double Z
)
```

### C++/CLI

```cpp
Component2^ InsertEnvelope(
   System.String^ CompName,
   System.String^ ConfigName,
   System.double X,
   System.double Y,
   System.double Z
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CompName`: Path and file name of file containing a part to insert as an envelope
- `ConfigName`: Name of the configuration from which to load the envelope component
- `X`: X coordinate of the center of the envelope component's bounding box
- `Y`: Y coordinate of the center of the envelope component's bounding box
- `Z`: Z coordinate of the center of the envelope component's bounding box

### Return Value

[IComponent2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2.html)

## VBA Syntax

See [AssemblyDoc::InsertEnvelope](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~InsertEnvelope.html).

## Remarks

CompName does not have to be open before running this method. If it is not open, then this method opens it in a hidden state.

If ConfigName is empty or specifies a configuration that does not exist, then the current configuration is used.

The X, Y, Z parameters of this method are the center of the component bounding box. You must use [IComponent2::Transform2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IComponent2~Transform2.html) on the return interface pointer if you want to more precisely position the component.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IComponent2::IsEnvelope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsEnvelope.html)
[IAssemblyDoc::AddComponent5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent5.html)
[IAssemblyDoc::AddComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents.html)
[IAssemblyDoc::IAddComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents2.html)
[IAssemblyDoc::ReplaceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14
