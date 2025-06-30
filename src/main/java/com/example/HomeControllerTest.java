// package com.example;

// import org.junit.jupiter.api.Test;
// import org.springframework.beans.factory.annotation.Autowired;
// import org.springframework.boot.test.context.SpringBootTest;
// import org.springframework.test.web.servlet.MockMvc;
// import org.springframework.test.web.servlet.request.MockMvcRequestBuilders;
// import org.springframework.test.web.servlet.result.MockMvcResultMatchers;

// @SpringBootTest
// public class HomeControllerTest {

//     @Autowired
//     private MockMvc mockMvc;

//     @Test
//     public void homePage_ShouldReturnWelcomeMessage() throws Exception {
//         mockMvc.perform(MockMvcRequestBuilders.get("/"))
//                 .andExpect(MockMvcResultMatchers.status().isOk())  // Check HTTP status is 200
//                 .andExpect(MockMvcResultMatchers.content().string("Welcome to E-Commerce Home Page!"));  // Check response content
//     }
// }
