---
title: "Get Edge Data By Name Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Edge_Data_By_Name_Example_CPlusPlus_COM.htm"
---

# Get Edge Data By Name Example (C++ COM)

This example shows how to get an edge by its name and then get the underlying curve parameters and curve length. Import swconst.tlb.

IEdge::IGetCurveParams2 returns an array, so this code must be used in an in-process DLL. Otherwise, use IEdge::GetCurveParams2 that returns a VARIANT.

```vb
void GetEdgeData(ISldWorks* m_pSldWorks)
{
 HRESULT res = NOERROR;
 LPMODELDOC2 p_ModelDoc = NULL;
 LPPARTDOC p_PartDoc = NULL;
 LPENTITY p_Entity = NULL;
 long doctype;

 // Retrieve the model document pointer
 res = m_pSldWorks->get_IActiveDoc2( &p_ModelDoc );
 if( res != S_OK || p_ModelDoc == NULL ) return;

 res = p_ModelDoc->GetType(&doctype);
 if (doctype != swDocPART )return;

 res = p_ModelDoc->QueryInterface(IID_IPartDoc, (LPVOID *)&p_PartDoc);

 res = p_ModelDoc->GetType(&doctype);
 if (doctype != swDocPART )return;

 // Get an entity by its name "FredsEdge"
 res = p_PartDoc->IGetEntityByName(_T("FredsEdge"), swSelEDGES, &p_Entity);

 if (res == S_OK && p_Entity != NULL)// If entity was found successfully
 {
  LPEDGE p_Edge = NULL;  // See if Entity is an Edge
  res = p_Entity->QueryInterface( IID_IEdge, (LPVOID*)&p_Edge);

  if (res == S_OK && p_Edge != NULL) // If Entity is an Edge
  {
   LPCURVE p_Curve;
   // Get the edge's underlying curve
   res = p_Edge->IGetCurve(&p_Curve);

   // Since we do not keep the curve parameters with every edge, this call is required or else the underlying curve parameters will be unknown.
   double edgeData[10]={NULL};
   // Get Edge data
   res = p_Edge->IGetCurveParams2(&edgeData[0]);

   // Setup for ints packed into doubles
    union PackedInts
   {
    double value;
    int intData[2];

   } packedIntData;

   // Get the integers from the double
   packedIntData.value = edgeData[8];
   int Notused = packedIntData.intData[0];
   int curveType = packedIntData.intData[1];
   // Get the integers from the double
   packedIntData.value = edgeData[9];        int Notused2 = packedIntData.intData[0];
   int curveTag = packedIntData.intData[1];

   CString message = _T("Attribute is on Edge with:\n");

message.Format(_T("\tStartPt = \t%lf \t%lf \t%lf \n \tEndPt  = \t%lf \t%lf \t%lf \n\tParams = \t%lf \t%lf \n\tCurveType = \t%i \n\tCurveTag = \t%i"),
     edgeData[0], edgeData[1], edgeData[2],
     edgeData[3], edgeData[4], edgeData[5],
     edgeData[6], edgeData[7],
     curveType, curveTag);
   AfxMessageBox( message );

   // Get the length of the underlying curve
   double curveLength;
   res = p_Curve->GetLength(edgeData[6], edgeData[7],
&curveLength);
   message = _T("The Edge length is:\n");
   message.Format(_T("\t%lf"), curveLength);
   AfxMessageBox( message );

   p_Curve->Release();

  // End if we got the Edge object
  }

  p_Edge->Release();
  p_Entity->Release();

 // End if we got the Entity by its name
 }

 p_PartDoc->Release();
 p_ModelDoc->Release();

// End of function
}
```
